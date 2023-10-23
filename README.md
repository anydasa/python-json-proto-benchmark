# JSON (orjson) vs Protobuf vs Arvo serialization benchmark

This repository contains a performance comparison between ORJSON and Protocol Buffers and ARVO in Python, utilizing dataclasses. The performance test is conducted on 10,000 iterations for serialization and deserialization, and a separate test is conducted for evaluating the size of the serialized data.

## Results

- Time taken for 10,000 iterations:
  - JSON Duration: 0.019 seconds
  - Protobuf Duration: 0.036 seconds
  - Arvo Duration: 0.20 seconds

- Size of serialized data:
  - JSON Size: 217 bytes
  - Protobuf Size: 65 bytes
  - Arvo Size: 81 bytes

## How to Run the Test

1. Clone the repository.
2. Install the necessary dependencies using `pip install -r requirements.txt`.
3. Run the test script using `python src/benchmark.py`.

### DTO FutureKline

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

json_size = sys.getsizeof(kline.to_json())
proto_size = sys.getsizeof(kline.to_proto())

print(f"JSON Size: {json_size} bytes")
print(f"Protobuf Size: {proto_size} bytes")
```
Result
```shell
JSON Duration: 0.01618671417236328 seconds
Protobuf Duration: 0.023717641830444336 seconds
Arvo Duration: 0.20125746726989746 seconds

JSON Size: 217 bytes
Protobuf Size: 65 bytes
Arvo Size: 81 bytes
```