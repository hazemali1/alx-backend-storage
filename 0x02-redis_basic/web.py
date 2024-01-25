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
    for i in range(len(d)):
        print(r.get("count:{}".format(d[i])))
        r.setex("count:{}".format(d[i]), 10, len(d))
        r.incr("count:{}".format(d[i]))
        print(d[i])
        print(r.get("count:{}".format(d[i])))
    return s


if __name__ == "__main__":
    """main"""
    print(get_page('http://slowwly.robertomurray.co.uk'))
