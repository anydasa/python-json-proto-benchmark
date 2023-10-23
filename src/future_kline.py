from dataclasses import dataclass

import avro
from avro.schema import Parse
from orjson import orjson

import future_kline_pb2

from avro.io import DatumReader, DatumWriter
import io

avro_schema = Parse("""
{
    "type": "record",
    "name": "FutureKline",
    "fields": [
        {"name": "exchange", "type": "string"},
        {"name": "symbol", "type": "string"},
        {"name": "event_time", "type": "long"},
        {"name": "timeframe", "type": "string"},
        {"name": "open_time", "type": "long"},
        {"name": "open_price", "type": "float"},
        {"name": "close_price", "type": "float"},
        {"name": "high_price", "type": "float"},
        {"name": "low_price", "type": "float"},
        {"name": "volume", "type": "float"}
    ]
}
""")


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

    def to_json(self):
        return orjson.dumps(self)

    @classmethod
    def from_json(cls, string: str):
        data = orjson.loads(string)
        return cls(**data)

    def to_proto(self):
        proto = future_kline_pb2.FutureKline()
        proto.exchange = self.exchange
        proto.symbol = self.symbol
        proto.event_time = self.event_time
        proto.timeframe = self.timeframe
        proto.open_time = self.open_time
        proto.open_price = self.open_price
        proto.close_price = self.close_price
        proto.high_price = self.high_price
        proto.low_price = self.low_price
        proto.volume = self.volume
        return proto.SerializeToString()

    @classmethod
    def from_proto(cls, proto_string: str):
        proto = future_kline_pb2.FutureKline()
        proto.ParseFromString(proto_string)
        return cls(
            exchange=proto.exchange,
            symbol=proto.symbol,
            event_time=proto.event_time,
            timeframe=proto.timeframe,
            open_time=proto.open_time,
            open_price=proto.open_price,
            close_price=proto.close_price,
            high_price=proto.high_price,
            low_price=proto.low_price,
            volume=proto.volume
        )

    def to_avro(self):
        writer = DatumWriter(avro_schema)
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(self.__dict__, encoder)
        return bytes_writer.getvalue()

    @classmethod
    def from_avro(cls, avro_bytes):
        reader = DatumReader(avro_schema)
        bytes_reader = io.BytesIO(avro_bytes)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        avro_dict = reader.read(decoder)
        return cls(**avro_dict)
