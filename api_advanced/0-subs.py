#!/usr/bin/python3
""""Doc"""
import requests


def number_of_subscribers(subreddit):
    """"Doc"""
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'}) \
        .json()
    subscribers_count = res.get('data').get('subscribers')
    return subscribers_count if subscribers_count is not None else 0
