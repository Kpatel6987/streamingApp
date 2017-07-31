import time
import schedule
from googlefinance import getQuotes
from streamingApp.producer.kafka_producer import Producer


def get_realtime_data(symbol):
    return getQuotes(symbol)[0]


def send_realtime_data(symbol, producer):
    producer.send(get_realtime_data(symbol))


def main(symbol):
    producer = Producer('my-topic')
    schedule.every(1).second.do(send_realtime_data, symbol, producer)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main('AAPL')
