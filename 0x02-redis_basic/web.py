#!/usr/bin/env python3
"""redis"""
import redis
import requests


def get_page(url: str) -> str:
    """get page"""
    return requests.get(url).text


if __name__ == "__main__":
    """main"""
    get_page('http://slowwly.robertomurray.co.uk')
