#!/usr/bin/env python3
"""redis"""
import redis
import requests
import re


def count_urls(html_content):
    """count urls"""
    url_pattern = re.compile(r'href=["\'](https?://\S+?)["\']', re.IGNORECASE)
    urls = re.findall(url_pattern, html_content)

    return urls


def get_page(url: str) -> str:
    """get page"""
    s = requests.get(url).text
    d = count_urls(s)
    r = redis.Redis()
    print(r.get("count:{}".format(d[0])))
    r.setex("count:{}".format(d[0]), 10, len(d))
    r.setex("count:{}".format("http://google.com"), 10, 1)
    r.setex("http://google.com", 10, 1)
    r.incr("count:{}".format(d[0]))
    print(d[0])
    print(r.get("count:{}".format(d[0])))
    return s


if __name__ == "__main__":
    """main"""
    print(get_page('http://slowwly.robertomurray.co.uk'))
