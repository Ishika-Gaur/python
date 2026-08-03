"""
====================================================
PROJECT : Hacker News Scraper (Part 4)

GOAL:
1. Hacker News se Title, Link aur Points nikalna.
2. Sirf 100+ points wali stories rakhna.
3. Data ko clean dictionary format me print karna.

====================================================
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint


# -------------------------------------------------
# Download Hacker News HTML
# -------------------------------------------------

response = requests.get("https://news.ycombinator.com/")

# HTML -> BeautifulSoup Object
soup = BeautifulSoup(response.text, "html.parser")


# -------------------------------------------------
# Grab Required Elements
# -------------------------------------------------

# Story links
links = soup.select(".titleline > a")

# Har story ka subtext (author, points, age etc.)
subtext = soup.select(".subtext")


# -------------------------------------------------
# Create Custom Hacker News
# -------------------------------------------------

def create_custom_hackernews(links, subtext):

    hacker_news = []

    # enumerate() -> index + current item
    for idx, item in enumerate(links):

        # -------------------------
        # Story Title
        # -------------------------
        title = item.getText()

        # -------------------------
        # Story Link
        # -------------------------
        href = item.get("href", None)

        # -------------------------
        # Score Element
        # score class subtext ke andar hoti hai
        # -------------------------

        vote = subtext[idx].select(".score")

        # Agar vote exist karta hai tabhi continue
        if len(vote):

            # Example:
            # "375 points"
            # -> "375"
            # -> 375

            points = int(
                vote[0].getText().replace(" points", "")
            )

            # Sirf 100+ points wali stories
            if points > 99:

                hacker_news.append({

                    "title": title,

                    "link": href,

                    "points": points

                })

    return hacker_news


# -------------------------------------------------
# Function Call
# -------------------------------------------------

news = create_custom_hackernews(
    links,
    subtext
)


# -------------------------------------------------
# Pretty Print
# -------------------------------------------------

pprint(news)