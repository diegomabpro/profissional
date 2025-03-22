from google.cloud import pubsub_v1
from config import PROJECT_ID, TOPIC_NAME

def publish_message(project_id: str, topic_name: str, message: str):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)
    future = publisher.publish(topic_path, message.encode("utf-8"))
    future.result()

if __name__ == "__main__":
    test_message = "Teste de mensagem no Pub/Sub"
    publish_message(PROJECT_ID, TOPIC_NAME, test_message)