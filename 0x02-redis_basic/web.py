#!/usr/bin/env python3
"""redis"""
import redis
import requests
from bs4 import BeautifulSoup


def count_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    anchor_tags = soup.find_all('a')
    num_urls = len(anchor_tags)
    print(html_content)
    return num_urls


def get_page(url: str) -> str:
    """get page"""
    return count_urls(requests.get(url).text)


if __name__ == "__main__":
    """main"""
    print(get_page('http://slowwly.robertomurray.co.uk'))
