#!/usr/bin/env python3
"""Implementing an expiring web cache and tracker"""
import requests
from functools import wraps
from time import time

cache = {}

def cached(func):
    @wraps(func)
    def wrapper(url):
        cache_key = f"count:{url}"
        now = time()
        if cache_key in cache and cache[cache_key]["expire"] > now:
            return cache[cache_key]["content"]
        else:
            content = func(url)
            cache[cache_key] = {"content": content, "expire": now + 10}
            return content
    return wrapper

@cached
def get_page(url: str) -> str:
    print(f"Fetching content for {url}")
    response = requests.get(url)
    return response.text

# Example usage
print(get_page("http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.example.com"))
print(get_page("http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.example.com"))
