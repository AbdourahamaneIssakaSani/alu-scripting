#!/usr/bin/python3
""""Doc"""
import requests


def recurse(subreddit, hot_list=[]):
    """"Doc
    Reddit sends an after property in the response.
    Keep retrieving comments until after is null.
    """
    url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)

    res = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0'})
    if res.status_code != 200:
        return None
    else:
        json_res = res.json()
        has_next = json_res.get('data').get('after') is not None
        hot_articles = json_res.get('data').get('children')
        [hot_list.append(article.get('data').get('title'))
         for article in hot_articles]
        if has_next:
            recurse(subreddit, hot_list)
        else:
            return hot_list if len(hot_list) > 0 else None
