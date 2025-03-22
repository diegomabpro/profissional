import pandas as pd
from google.cloud import storage
from config import BUCKET_NAME, RAW_ZONE_PREFIX, TRUSTED_ZONE_PREFIX

def load_from_gcs(file_name: str) -> pd.DataFrame:
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"{RAW_ZONE_PREFIX}/{file_name}")
    data = pd.read_csv(blob.download_as_string())
    return data

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by='Date')
    return data

def save_to_gcs(data: pd.DataFrame, file_name: str):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"{TRUSTED_ZONE_PREFIX}/{file_name}")
    blob.upload_from_string(data.to_csv(index=False), content_type='text/csv')

def main(file_name: str):
    try:
        raw_data = load_from_gcs(file_name)
        transformed_data = transform_data(raw_data)
        save_to_gcs(transformed_data, file_name)
    except Exception as e:
        print(f"Erro durante a transformação: {e}")

if __name__ == "__main__":
    file_name = "BTC-USD_data.csv"
    main(file_name)