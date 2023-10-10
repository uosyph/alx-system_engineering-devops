#!/usr/bin/python3
"""
Prints a sorted list of the number of times each keyword
in a given list occurs in the hot posts of a given subreddit.
"""

import requests


def sort_histogram(histogram={}):
    """Sorts and prints the given histogram."""

    histogram = list(filter(lambda kv: kv[1], histogram))
    histogram_dict = {}

    for item in histogram:
        if item[0] in histogram_dict:
            histogram_dict[item[0]] += item[1]
        else:
            histogram_dict[item[0]] = item[1]

    histogram = list(histogram_dict.items())
    histogram.sort(key=lambda kv: kv[0], reverse=False)
    histogram.sort(key=lambda kv: kv[1], reverse=True)

    keyword_count = "\n".join(list(map(
                                    lambda kv: f"{kv[0]}: {kv[1]}", histogram
                                    )))
    if keyword_count:
        print(keyword_count)


def count_words(subreddit, word_list, histogram=[], count=0, after=None):
    """
    Queries the Reddit API and parses the titles of all hot articles
    in a given subreddit, then counts the number of times each keyword
    in a given list occurs (case-insensitively, delimited by spaces, e.g.,
    "Javascript" should count as "javascript", but "java" should not).
    """

    url = f"https://www.reddit.com/r/{subreddit}/.json"
    headers = {
        "Accept": "application/json",
        "User-Agent": "linux:0x16.api.advanced"
    }
    sort = "hot"
    limit = 30
    params = {
        "sort": sort,
        "limit": limit,
        "count": count,
        "after": after if after else "",
    }
    response = requests.get(
        url=url, headers=headers, params=params, allow_redirects=False
    )

    if not histogram:
        word_list = list(map(lambda word: word.lower(), word_list))
        histogram = list(map(lambda word: (word, 0), word_list))

    if response.status_code != 200:
        return

    data = response.json()["data"]
    posts = data["children"]
    titles = list(map(lambda post: post["data"]["title"], posts))
    histogram = list(
        map(
            lambda kv: (
                kv[0],
                kv[1] + sum(list(map(
                        lambda word: word.lower().split().count(kv[0]), titles
                        ))),
            ),
            histogram,
        )
    )

    if len(posts) >= limit and data["after"]:
        count_words(
            subreddit, word_list, histogram, count + len(posts), data["after"]
        )
    else:
        sort_histogram(histogram)
