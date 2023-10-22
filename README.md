# orjson vs Protobuf Serialization Performance Test

This repository contains a performance comparison test between `orjson` and `Protobuf` for serializing and deserializing data in Python.

## Setup

- Python version used: 3.10
- Libraries used: `orjson`, `protobuf`

## Test Procedure

The `FutureKline` class is serialized and deserialized using both `orjson` and `Protobuf` over 10,000 iterations to measure the time taken for each operation.

## Results

- The following results were obtained:

  - **Serialization/Deserialization Duration**:
    - **orjson**: 0.0190 seconds
    - **Protobuf**: 0.0364 seconds

  - **Data Size**:
    - **orjson**: 217 bytes
    - **Protobuf**: 65 bytes

## Conclusion

From the test, it's observed that `orjson` is faster in serialization/deserialization compared to `Protobuf`. However, `Protobuf` significantly reduces the data size, which could be beneficial in network communication or storage.

