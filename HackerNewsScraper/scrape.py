"""
===========================================
PROJECT : Hacker News Scraper

GOAL:
Download Hacker News HTML using Requests.
Later BeautifulSoup will extract stories,
links and points.

===========================================
"""

# Website se HTML download karne ke liye
import requests

# HTML ko parse karne ke liye
from bs4 import BeautifulSoup


# Hacker News page ka HTML download karo
response = requests.get(
    "https://news.ycombinator.com/"
)

# Server ka status code check karo
print(response)

# Downloaded HTML print karo
print(response.text)