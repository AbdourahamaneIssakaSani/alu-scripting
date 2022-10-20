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
    subscribers_count = res.get('data').get('subscribers') \
        if res.get('data').get('subscribers') is not None else 0
    return subscribers_count
