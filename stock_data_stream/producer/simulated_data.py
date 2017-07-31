import json
import time
from stock_data_stream.producer.kafka_producer import Producer


def get_simulated_data(symbol):
    data_list = parse_file(symbol)
    write_file(data_list, symbol)
    return data_list


def parse_file(symbol):
    file = '../resources/' + symbol + '.json'
    data_list = []
    with open(file) as json_file:
        data = json.load(json_file)
        for value in data['Time Series (1min)']:
            price_dict = {'LastTradeDateTime': value.replace(" ", "T") + "Z", 'StockSymbol': symbol,
                          'LastTradePrice': data['Time Series (1min)'][value]['4. close']}
            data_list.append(price_dict)
    json_file.close()
    data_list.sort(key=lambda item: item['LastTradeDateTime'], reverse=True)
    return data_list


def write_file(data_list, symbol):
    last_date = data_list[0]['LastTradeDateTime'].split('T')[0]
    f = open('../resources/' + symbol + last_date + '.txt', 'w')
    f.write(str(data_list))
    f.close()


def send_simulated_data(producer, data_list):
    for data in data_list:
        producer.send(data)
        time.sleep(10)


def main(symbol):
    producer = Producer('my-topic')
    send_simulated_data(producer, get_simulated_data(symbol))


if __name__ == '__main__':
    main('AAPL')
