#!/usr/bin/python3
""" Module for retrieving employee TODO list information using an API """

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """ Function to fetch and display employee TODO list progress """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos".format(base_url)

    employee_data = requests.get(employee_url).json()
    employee_name = employee_data['name']
    todo_list = requests.get(todo_url, params={"userId": employee_id}).json()

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
    fetch_employee_todo_progress(employee_id)