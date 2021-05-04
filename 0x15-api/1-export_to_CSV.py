#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def gather_data():
    """
    Script to return information from REST API
    """
    user_id_param = int(sys.argv[1])
    # r is a Response object from users
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(user_id_param))
    # t is a Response object from TODO
    t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(user_id_param))

    # To convert a Response object to an iterable python object (dict or list)
    obj = r.json()
    obj_2 = t.json()

    # To get user_name
    user_name = obj['username']

    with open('{}.csv'.format(user_id_param), 'w', newline='') as csv_file:
        writer = csv.writer(
            csv_file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL)

        for i in range(len(obj_2)):
            status_task = obj_2[i]['completed']
            title = obj_2[i]['title']
            writer.writerow([user_id_param, user_name, status_task, title])


if __name__ == '__main__':
    gather_data()
