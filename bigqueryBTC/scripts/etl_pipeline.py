from extract import main as extract_main
from transform import main as transform_main
from load import main as load_main
from pubsub import publish_message
from config import PROJECT_ID, TOPIC_NAME, TICKER, START_DATE, END_DATE

def run_etl_pipeline():
    try:
        extract_main(TICKER, START_DATE, END_DATE, f"{TICKER}_data.csv")
        transform_main(f"{TICKER}_data.csv")
        load_main(f"{TICKER}_data.csv", "bigquerybtc_trusted")
        publish_message(PROJECT_ID, TOPIC_NAME, "Pipeline de ETL executado com sucesso!")
    except Exception as e:
        publish_message(PROJECT_ID, TOPIC_NAME, f"Erro no pipeline de ETL: {str(e)}")

if __name__ == "__main__":
    run_etl_pipeline()