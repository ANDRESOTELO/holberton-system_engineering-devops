#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import json
import requests
import sys


def export_json_data():
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

    user_name = obj['username']
    dictio_in_list = {}
    list_of_dictio = []

    for i in range(len(obj_2)):
        status_task = obj_2[i]['completed']
        title = obj_2[i]['title']
        dictio_in_list = {'task': title,
                          'completed': status_task,
                          'username': user_name}
        list_of_dictio.append(dictio_in_list)
    json_dictio = {user_id_param: list_of_dictio}

    with open('{}.json'.format(user_id_param), 'w') as json_file:
        json.dump(json_dictio, json_file)

if __name__ == '__main__':
    export_json_data()
