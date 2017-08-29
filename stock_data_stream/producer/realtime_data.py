import time
import schedule
from googlefinance import getQuotes
from kafka_producer import Producer


def get_realtime_data(symbol):
    return getQuotes(symbol)[0]


def send_realtime_data(producer):
    f = open("../resources/sp500list.csv")
    symbols = f.readlines()
    for line in symbols:
        symbol = line.split(",")
        producer.send(get_realtime_data(symbol[0]))


def main(symbol):
    producer = Producer('my-topic')
    schedule.every(5).minutes.do(send_realtime_data, producer)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main('AAPL')
