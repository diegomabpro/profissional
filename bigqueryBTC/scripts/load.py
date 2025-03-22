from google.cloud import bigquery
from google.cloud import storage
from config import BUCKET_NAME, TRUSTED_ZONE_PREFIX, DATASET_NAME, RAW_TABLE_NAME, TRUSTED_TABLE_NAME, REFINED_TABLE_NAME

def load_to_bigquery(file_name: str, table_name: str):
    client = bigquery.Client()
    dataset_ref = client.dataset(DATASET_NAME)
    table_ref = dataset_ref.table(table_name)
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )
    uri = f"gs://{BUCKET_NAME}/{TRUSTED_ZONE_PREFIX}/{file_name}"
    load_job = client.load_table_from_uri(uri, table_ref, job_config=job_config)
    load_job.result()

def main(file_name: str, table_name: str):
    try:
        load_to_bigquery(file_name, table_name)
    except Exception as e:
        print(f"Erro durante o carregamento: {e}")

if __name__ == "__main__":
    file_name = "BTC-USD_data.csv"
    table_name = TRUSTED_TABLE_NAME
    main(file_name, table_name)