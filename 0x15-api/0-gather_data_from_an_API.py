#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def gather_data():
    """
    Script to return information from REST API
    """
    param = int(sys.argv[1])
    # r is a Response object from users
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                     .format(param))
    # t is a Response object from TODO
    t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                     .format(param))

    # To convert a Response object to an iterable python object (dict or list)
    obj = r.json()
    obj_2 = t.json()
    # To count done tasks
    done_task = 0
    total_task = len(obj_2)

    for i in range(len(obj_2)):
        if obj_2[i]['completed'] is True:
            done_task += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(obj['name'], done_task, total_task))

    for i in range(len(obj_2)):
        if obj_2[i]['completed'] is True:
            print('\t {}'.format(obj_2[i]['title']))


if __name__ == '__main__':
    gather_data()
