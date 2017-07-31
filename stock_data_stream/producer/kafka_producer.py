import json
from kafka import KafkaProducer


class Producer:

    def __init__(self, topic):
        self.producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                      bootstrap_servers='localhost:9092')
        self.topic = topic

    def send(self, data):
        self.producer.send(self.topic, data)





