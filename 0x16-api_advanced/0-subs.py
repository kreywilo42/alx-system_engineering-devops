#!/usr/bin/python3
"""querying number_of_subscribers from reddit api"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subcribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('https://www.reddit.com/r/{}/about.json'.format
                     (subreddit), headers={'User-Agent': 'alx-api_advanced\
                         :project:v1.0.0 (by /u/Just_boj)'}).json()
    sub_result = r.get("data", {}).get("subscribers", 0)
    return sub_result
