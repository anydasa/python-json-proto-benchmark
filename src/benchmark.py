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
    FutureKline.from_json(kline.to_json())
json_duration = time.time() - start_time

start_time = time.time()
for _ in range(10000):
    FutureKline.from_proto(kline.to_proto())
proto_duration = time.time() - start_time


start_time = time.time()
for _ in range(10000):
    FutureKline.from_avro(kline.to_avro())
arvo_duration = time.time() - start_time


print(f"JSON Duration: {json_duration} seconds")
print(f"Protobuf Duration: {proto_duration} seconds")
print(f"Arvo Duration: {arvo_duration} seconds")

print(f"JSON Size: {sys.getsizeof(kline.to_json())} bytes")
print(f"Protobuf Size: {sys.getsizeof(kline.to_proto())} bytes")
print(f"Arvo Size: {sys.getsizeof(kline.to_avro())} bytes")
