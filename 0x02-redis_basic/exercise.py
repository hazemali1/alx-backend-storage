#!/usr/bin/env python3
"""redis"""
import redis
import uuid
import typing
from functools import wraps


def call_history(method: typing.Callable) -> typing.Callable:
    """history"""
    @wraps(method)
    def wrapper(self: typing.Any, *args) -> str:
        """wrapper functool.wraps"""
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        output = method(self, *args)
        self._redis.rpush("{}:outputs".format(method.__qualname__), output)
        return output
    return wrapper


def count_calls(method: typing.Callable) -> typing.Callable:
    """count calls for cache class"""
    @wraps(method)
    def wrapper(self: typing.Any, *args, **kwds) -> str:
        """wrapper functool.wraps"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper


class Cache():
    """Cache class"""
    def __init__(self):
        """initialize the cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
        return self._redis.get(key)

    def get_str(self, key: bytes) -> str:
        """strin"""
        return key.decode("utf-8")

    def get_int(self, key: bytes) -> str:
        """integer"""
        return int(key)
