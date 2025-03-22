# Configurações do Projeto bigqueryBTC

# Google Cloud Storage (GCS)
BUCKET_NAME = "bigquerybtc-bucket"
RAW_ZONE_PREFIX = "raw"
TRUSTED_ZONE_PREFIX = "trusted"

# BigQuery
DATASET_NAME = "bigquerybtc_dataset"
RAW_TABLE_NAME = "bigquerybtc_raw"
TRUSTED_TABLE_NAME = "bigquerybtc_trusted"
REFINED_TABLE_NAME = "bigquerybtc_refined"

# Pub/Sub
PROJECT_ID = "bigqueryBTC"
TOPIC_NAME = "bigquerybtc-topic"

# Yahoo Finance API
TICKER = "BTC-USD"
START_DATE = "2010-01-01"
END_DATE = "2024-12-31"