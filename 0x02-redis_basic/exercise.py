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
