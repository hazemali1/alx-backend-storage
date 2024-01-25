#!/usr/bin/env python3
"""redis"""
import redis
import requests


def count_urls(html_content):
    # soup = BeautifulSoup(html_content, 'html.parser')
    # urls = [a.get('href') for a in soup.find_all('a', href=True)]
    # print(urls)
    return len(html_content)


def get_page(url: str) -> str:
    """get page"""
    s = requests.get(url).text
    count_urls(s)
    return s


if __name__ == "__main__":
    """main"""
    print(get_page('http://slowwly.robertomurray.co.uk'))
