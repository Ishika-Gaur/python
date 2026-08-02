"""
=========================================================
PROJECT : Twitter Bot (2026)

GOAL:
1. Connect with X (Twitter) API
2. Authenticate User
3. Read Logged-in User Information

=========================================================
"""

import tweepy
import os
from dotenv import load_dotenv

# .env file load karo
load_dotenv()

# Credentials
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Client Create
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

try:

    # Logged-in user ki information
    me = client.get_me(
        user_fields=["username", "name", "public_metrics"]
    )

    print("Connected Successfully\n")

    print("Name :", me.data.name)

    print("Username :", me.data.username)

except Exception as e:

    print("Error :")
    print(e)