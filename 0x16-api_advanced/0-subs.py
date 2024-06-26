#!/usr/bin/python3
"""
Find the number of subscribers of a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Send a request to find number of subsribers

    Returns:
        - number of subscriber
        - otherwise zero
    """
    if subreddit is None:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'alx_task'}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            n = int(res.json().get('data').get('subscribers'))
            return n
        return 0
    except Exception:
        return 0
