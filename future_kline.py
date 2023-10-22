from dataclasses import dataclass
from orjson import orjson

from src import future_kline_pb2


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
        proto = future_kline_pb2.FutureKline()  # Создайте объект FutureKline
        proto.ParseFromString(proto_string)  # Разберите строку с этим объектом
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
