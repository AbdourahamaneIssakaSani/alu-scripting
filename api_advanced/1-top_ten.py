#!/usr/bin/python3
def top_ten(subreddit):
    """"Doc"""
    url = "https://www.reddit.com/r/{}/top.json?limit=10" \
        .format(subreddit)

    res = requests.get(url,
                       headers={
                           'User-Agent': 'Mozilla/5.0'})

    if res.status_code != 200:
        print(None)
    else:
        json_response = res.json()
        posts = json_response.get('data').get('children')
        [print(post.get('data').get('title')) for post in posts]
