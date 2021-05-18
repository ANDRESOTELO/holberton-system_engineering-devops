#!/usr/bin/python3
"""
Top Ten
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given
    subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    next_page = {"after": after}
    request = requests.get(url,
                           headers={'User-agent': 'myapp/1.0'},
                           allow_redirects=False,
                           params=next_page)
    if request.status_code != 200:
        return None
    try:
        response = request.json()
        if response:
            data = response.get('data')
            after = data.get('after')
            children = data.get('children')

            for child in children:
                children_data = child.get('data')
                title = children_data.get('title')
                if title:
                    hot_list.append(title)
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except:
        print(None)
