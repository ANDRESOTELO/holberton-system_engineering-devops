#!/usr/bin/python3
"""
Top Ten
"""
import requests


def top_ten(subreddit):
    """Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit"""
    try:
        url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
        request = requests.get(url,
                               headers={'User-agent': 'myapp/1.0'},
                               allow_redirects=False)
        if request.status_code == 200:
            response = request.json()
            if response:
                data = response.get('data')
                children = data.get('children')

                for child in children:
                    children_data = child.get('data')
                    print(children_data.get('title'))
        print(None)
    except(BaseException):
        print(None)
