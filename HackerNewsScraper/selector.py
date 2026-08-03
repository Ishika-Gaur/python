import requests

from bs4 import BeautifulSoup

response = requests.get(
    "https://news.ycombinator.com/"
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

# Sab links
links = soup.select(".titleline > a")

# Sab votes
votes = soup.select(".score")

print(links)

print(votes)

# Pehla link
print(links[0])

# Pehla vote
print(votes[0])

# Vote ka ID
print(votes[0].get("id"))