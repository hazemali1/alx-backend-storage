#!/usr/bin/env python3
"""redis"""
import redis
import requests

r = redis.Redis()  # Create a Redis client instance (outside the function for efficiency)

def get_page(url: str) -> str:
    """Retrieves a page's content, caches it with an expiration time, and tracks access count."""

    cached_value = r.get("cached:{}".format(url))
    if cached_value:
        return cached_value.decode("utf-8")  # Decode the cached value if it exists

    r.incr("count:{}".format(url))  # Increment the access count
    response = requests.get(url)
    page_content = response.text
    r.setex("cached:{}".format(url), 10, page_content)  # Cache the content for 10 seconds
    return page_content

if __name__ == "__main__":
    page_content = get_page("http://slowwly.robertomurray.co.uk")
    print(page_content)
