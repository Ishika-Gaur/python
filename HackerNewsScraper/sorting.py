"""
====================================================
PROJECT : Hacker News Scraper

GOAL:
1. Hacker News scrape karna.
2. Title, Link aur Votes nikalna.
3. Sirf 100+ votes wali stories rakhna.
4. Stories ko Highest Votes -> Lowest Votes sort karna.
====================================================
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint


# ----------------------------------------
# Download Hacker News HTML
# ----------------------------------------

response = requests.get("https://news.ycombinator.com/")

# HTML ko BeautifulSoup object me convert karo
soup = BeautifulSoup(response.text, "html.parser")


# ----------------------------------------
# Required Elements
# ----------------------------------------

# Story links
links = soup.select(".titleline > a")

# Story ke niche wala section
subtext = soup.select(".subtext")


# ----------------------------------------
# Sort Stories by Votes
# ----------------------------------------

def sort_stories_by_votes(hacker_news_list):
    """
    votes ke according highest -> lowest sort karega
    """

    return sorted(
        hacker_news_list,
        key=lambda story: story["points"],
        reverse=True
    )


# ----------------------------------------
# Create Custom Hacker News
# ----------------------------------------

def create_custom_hackernews(links, subtext):

    hacker_news = []

    for idx, item in enumerate(links):

        # Story Title
        title = item.getText()

        # Story URL
        href = item.get("href", None)

        # Score element
        vote = subtext[idx].select(".score")

        # Agar score exist karta hai
        if len(vote):

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

    # Sorted List Return
    return sort_stories_by_votes(hacker_news)


# ----------------------------------------
# Function Call
# ----------------------------------------

news = create_custom_hackernews(
    links,
    subtext
)

# Pretty Print
pprint(news)