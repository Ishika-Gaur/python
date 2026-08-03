"""
====================================================
PROJECT : Hacker News Scraper

GOAL:
1. Hacker News scrape karna.
2. Page 1 + Page 2 dono scrape karna.
3. Sirf 100+ points wali stories dikhana.
4. Highest points ke according sort karna.
====================================================
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint


# -------------------------------------------------
# Page 1 Download
# -------------------------------------------------

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")


# -------------------------------------------------
# Page 2 Download
# -------------------------------------------------

response2 = requests.get("https://news.ycombinator.com/?p=2")
soup2 = BeautifulSoup(response2.text, "html.parser")


# -------------------------------------------------
# Page 1 Data
# -------------------------------------------------

links = soup.select(".titleline > a")
subtext = soup.select(".subtext")


# -------------------------------------------------
# Page 2 Data
# -------------------------------------------------

links2 = soup2.select(".titleline > a")
subtext2 = soup2.select(".subtext")


# -------------------------------------------------
# Dono pages combine karo
# -------------------------------------------------

mega_links = links + links2

mega_subtext = subtext + subtext2


# -------------------------------------------------
# Sort Function
# -------------------------------------------------

def sort_stories_by_votes(hacker_news_list):

    return sorted(
        hacker_news_list,
        key=lambda story: story["points"],
        reverse=True
    )


# -------------------------------------------------
# Create Custom Hacker News
# -------------------------------------------------

def create_custom_hackernews(links, subtext):

    hacker_news = []

    for idx, item in enumerate(links):

        title = item.getText()

        href = item.get("href", None)

        vote = subtext[idx].select(".score")

        if len(vote):

            points = int(
                vote[0].getText().replace(" points", "")
            )

            if points > 99:

                hacker_news.append({

                    "title": title,

                    "link": href,

                    "points": points

                })

    return sort_stories_by_votes(hacker_news)


# -------------------------------------------------
# Function Call
# -------------------------------------------------

news = create_custom_hackernews(
    mega_links,
    mega_subtext
)

pprint(news)