#!/usr/bin/env python3
"""redis"""
import redis
import requests
import re


def count_urls(html_content):
    """count urls"""
    url_pattern = re.compile(r'href=["\'](https?://\S+?)["\']', re.IGNORECASE)
    urls = re.findall(url_pattern, html_content)

    return len(urls)


def get_page(url: str) -> str:
    """get page"""
    s = requests.get(url).text
    print(count_urls(s))
    return s


if __name__ == "__main__":
    """main"""
    print(get_page('http://slowwly.robertomurray.co.uk'))
