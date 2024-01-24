#!/usr/bin/env python3
"""redis"""
import redis
import uuid
import typing


class Cache():
    """Cache class"""
    def __init__(self):
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes,  int,  float]) -> str:
        uid = str(uuid.uuid4())
        self._redis.set(uid, data)
        return uid

    def get(self, key: str, fn: typing.Optional[typing.Callable] = None) -> typing.Any:
        """get value"""
        if callable(fn):
            return fn(self._redis.get(key))
        if fn is str:
            return self.get_str(self._redis.get(key))
        if fn is int:
            return self.get_int(self._redis.get(key))

    def get_str(self, key: bytes) -> str:
        """strin"""
        return key.decode("utf-8")

    def get_int(self, key: bytes) -> str:
        """integer"""
        return int(key)
