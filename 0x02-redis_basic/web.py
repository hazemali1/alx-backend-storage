#!/usr/bin/env python3
"""redis"""
import redis
import requests
import re


def count_urls(html_content):
    # soup = BeautifulSoup(html_content, 'html.parser')
    # urls = [a.get('href') for a in soup.find_all('a', href=True)]
    # print(urls)
    url_pattern = re.compile(r'href=["\'](https?://\S+?)["\']', re.IGNORECASE)
    urls = re.findall(url_pattern, html_content)
    print(urls)

    s = 0
    if 'href="https://www.google.com"' in html_content:
        s += 1
    print(s)
    print(type(html_content))
    return len(html_content)


def get_page(url: str) -> str:
    """get page"""
    s = requests.get(url).text
    print(count_urls(s))
    return s


if __name__ == "__main__":
    """main"""
    print(get_page('http://slowwly.robertomurray.co.uk'))
