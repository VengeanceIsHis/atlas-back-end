#!/usr/bin/python3
"""Adding module documentation"""
from requests import requests
import sys


def get_employee_todo(employee_id):
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    employee_name = requests.get("name")
    user = requests.get(url + "users/{}".format(employee_id)).json()
    employee = user['name']

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        employee), len(completed), len(todos))

    # Print the completed tasks one by one with indentation
    [print("\t {}".format(complete)) for complete in completed]


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_id -= 1
