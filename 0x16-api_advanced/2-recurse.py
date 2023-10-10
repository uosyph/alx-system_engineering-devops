#!/usr/bin/python3
"""Returns a list of titles of all hot posts on a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit,
    the function should return None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(
        url=url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    [hot_list.append(t.get("data").get("title"))
     for t in results.get("children")]

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
