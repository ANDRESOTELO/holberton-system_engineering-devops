#!/usr/bin/python3
"""
API advanced
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        request = requests.get(url,
                               headers={'User-agent': 'myapp/1.0'},
                               allow_redirects=False)
        if request.status_code == 200:
            response = request.json()
            if response:
                data = response.get('data')
                if data:
                    return data.get('subscribers')
        return 0

    except:
        return 0
