#!/usr/bin/env python3
"""redis"""
import redis
import requests


def get_page(url: str) -> str:
    """get page"""
    redis.Redis().set("cached:{}".format(url), 0)
    redis.Redis().incr("count:{}".format(url))
    redis.Redis().setex("cached:{}".format(url), 10, redis.Redis().get("cached:{}".format(url)))
    return requests.get(url).text


if __name__ == "__main__":
    """main"""
    get_page('http://slowwly.robertomurray.co.uk')
