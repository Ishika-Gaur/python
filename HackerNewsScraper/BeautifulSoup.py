"""
=============================================
PROJECT : Hacker News Scraper

GOAL:
Download Hacker News HTML
and parse it using BeautifulSoup.

=============================================
"""

import requests

from bs4 import BeautifulSoup


# HTML download karo
response = requests.get(
    "https://news.ycombinator.com/"
)

# HTML ko parse karo
soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# Pura HTML
print(soup)

# Sirf body
print(soup.body)

# Body ke direct contents
print(soup.body.contents)

# Sab div tags
print(soup.find_all("div"))

# Sab links
print(soup.find_all("a"))

# Page title
print(soup.title)

# Pehla link
print(soup.a)

# Ya
print(soup.find("a"))