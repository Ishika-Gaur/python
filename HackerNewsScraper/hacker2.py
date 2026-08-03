"""
====================================================
PROJECT : Hacker News Scraper (Part 3)

GOAL:
1. Hacker News se Title, Link aur Points nikalna.
2. Sirf useful data ko dictionary me store karna.
3. Abhi filtering (100+ points) next step me karenge.

====================================================
"""

import requests
from bs4 import BeautifulSoup


# ---------------------------------------------------
# Step 1 : Hacker News page download karo
# ---------------------------------------------------

response = requests.get("https://news.ycombinator.com/")


# ---------------------------------------------------
# Step 2 : HTML ko BeautifulSoup object me convert karo
# ---------------------------------------------------

soup = BeautifulSoup(response.text, "html.parser")


# ---------------------------------------------------
# Step 3 : Sabhi story links aur votes nikalo
# ---------------------------------------------------

# Sabhi story links
links = soup.select(".titleline > a")

# Sabhi votes
votes = soup.select(".score")


# ---------------------------------------------------
# Function : Custom Hacker News List
# ---------------------------------------------------

def create_custom_hackernews(links, votes):

    hacker_news = []

    # enumerate() se index bhi milega
    for idx, item in enumerate(links):

        # -------------------------------
        # Story Title
        # -------------------------------
        title = links[idx].getText()

        # -------------------------------
        # Story Link
        # -------------------------------
        href = links[idx].get("href", None)

        # --------------------------------------------------
        # IMPORTANT
        # Kuch stories ke votes nahi hote.
        # Isliye check karna zaroori hai.
        # --------------------------------------------------

        if idx < len(votes):

            # Example:
            # "375 points"
            #        ↓
            # replace()
            #        ↓
            # "375"
            #        ↓
            # int()
            #        ↓
            # 375

            points = int(
                votes[idx].getText().replace(" points", "")
            )

        else:
            # Agar vote nahi mila
            points = 0

        # --------------------------------------------------
        # Dictionary bana kar list me add karo
        # --------------------------------------------------

        hacker_news.append({
            "title": title,
            "link": href,
            "points": points
        })

    return hacker_news


# ---------------------------------------------------
# Function Call
# ---------------------------------------------------

news = create_custom_hackernews(links, votes)


# ---------------------------------------------------
# Output
# ---------------------------------------------------

for story in news:
    print(story)