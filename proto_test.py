import sys
import time

from future_kline import FutureKline

kline = FutureKline(
    exchange='binance',
    symbol='BTCUSDT',
    event_time=123234234,
    timeframe='1m',
    open_time=234234324,
    open_price=0.0,
    high_price=0.0,
    low_price=0.0,
    close_price=0.0,
    volume=0.0,
)

start_time = time.time()
for _ in range(10000):
    json_data = kline.to_json()
    kline_from_json = FutureKline.from_json(json_data)
json_duration = time.time() - start_time

proto_kline = kline.to_proto()
start_time = time.time()
for _ in range(10000):
    proto_data = kline.to_proto()
    kline_from_proto = FutureKline.from_proto(proto_data)
proto_duration = time.time() - start_time

print(f"JSON Duration: {json_duration} seconds")
print(f"Protobuf Duration: {proto_duration} seconds")

json_size = sys.getsizeof(kline.to_json())
proto_size = sys.getsizeof(kline.to_proto())

print(f"JSON Size: {json_size} bytes")
print(f"Protobuf Size: {proto_size} bytes")
