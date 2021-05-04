#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import json
import requests


def export_json_data():
    """
    Script to return information from REST API
    """
    # r is a Response object from users
    r = requests.get('https://jsonplaceholder.typicode.com/users')

    # To convert a Response object to an iterable python object (dict or list)
    obj = r.json()
    json_dictio = {}

    for user in obj:

        user_id = user['id']
        user_name = user.get('username')

        t = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id))
        obj_2 = t.json()

        dictio_in_list = {}
        list_of_dictio = []

        for i in range(len(obj_2)):
            status_task = obj_2[i]['completed']
            title = obj_2[i]['title']
            dictio_in_list = {'task': title,
                              'completed': status_task,
                              'username': user_name}
            list_of_dictio.append(dictio_in_list)
        json_dictio[user_id] = list_of_dictio

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(json_dictio, json_file)

if __name__ == '__main__':
    export_json_data()
