import json
from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', group_id='view', bootstrap_servers=['localhost:9092'])


def consume():
    for msg in consumer:
        message = json.loads(msg.value.decode("utf-8"))
        print(message)

if __name__ == '__main__':
    consume()
