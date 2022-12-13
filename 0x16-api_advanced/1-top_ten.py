#!/usr/bin/python3

"""queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit"""


import requests


def top_ten(subreddit):
    """function to query top ten hot post"""
    headers = {
                "User-Agent": "alx-api_advanced:project:\
                v1.0.0 (by /u/Just_boj)"}
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
