#!/usr/bin/python3
"""New module based around handlings requests to url"""
import requests
import sys


def new_data_from_api(employee_id):
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    completed = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for complete in completed:
        print("\t{}".format(complete))

    return employee_id
