import pandas as pd
import yfinance as yf
from google.cloud import storage
from config import BUCKET_NAME, RAW_ZONE_PREFIX, TICKER, START_DATE, END_DATE

def extract_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def save_to_gcs(data: pd.DataFrame, file_name: str):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"{RAW_ZONE_PREFIX}/{file_name}")
    blob.upload_from_string(data.to_csv(index=False), content_type='text/csv')

def main():
    try:
        data = extract_data(TICKER, START_DATE, END_DATE)
        file_name = f"{TICKER}_data.csv"
        save_to_gcs(data, file_name)
    except Exception as e:
        print(f"Erro durante a extração: {e}")

if __name__ == "__main__":
    main()