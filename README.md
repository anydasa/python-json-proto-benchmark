# JSON (orjson) vs Protocol Buffers Performance Test (Python)

This repository contains a performance comparison between ORJSON and Protocol Buffers in Python, utilizing dataclasses. The performance test is conducted on 10,000 iterations for serialization and deserialization, and a separate test is conducted for evaluating the size of the serialized data.

## Results

- Time taken for 10,000 iterations:
  - JSON Duration: 0.019 seconds
  - Protobuf Duration: 0.036 seconds

- Size of serialized data:
  - JSON Size: 217 bytes
  - Protobuf Size: 65 bytes


## Dependencies

- orjson
- protobuf
- dataclasses (Python 3.10)

```python
@dataclass(frozen=True)
class FutureKline:
    exchange: str
    symbol: str
    event_time: int
    timeframe: str
    open_time: int
    open_price: float
    close_price: float
    high_price: float
    low_price: float
    volume: float

```

```python
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
```
Result
```shell
JSON Duration: 0.17911291122436523 seconds
Protobuf Duration: 0.339336633682251 seconds
JSON Size: 217 bytes
Protobuf Size: 65 bytes
```