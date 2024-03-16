#!/usr/bin/python3
""" Module for retrieving employee TODO list information using an API """

import json
import sys
import urllib.request


def fetch_employee_todo_progress(employee_id):
    """ Function to fetch and display employee TODO list progress """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos".format(base_url)

    with urllib.request.urlopen(employee_url) as response:
        employee_data = json.loads(response.read().decode())

    employee_name = employee_data['name']

    todo_url_with_params = "{}?userId={}".format(todo_url, employee_id)
    with urllib.request.urlopen(todo_url_with_params) as response:
        todo_list = json.loads(response.read().decode())

    completed_tasks = []
    total_tasks = 0
    for todo in todo_list:
        total_tasks += 1
        if todo["completed"]:
            completed_tasks.append(todo["title"])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task_title in completed_tasks:
        print("\t{}".format(task_title))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
