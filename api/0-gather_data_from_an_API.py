#!/usr/bin/python3
"""Next test for task 0"""
import requests
import sys


def retrieve_employee_name(emp_id):
    """
    Retrieves the name of the employee.
    """
    url = "{}/{}".format(base_url, emp_id)
    response = requests.get(url)
    return response.json().get("name")


def retrieve_assigned_tasks(emp_id):
    """
    Retrieves the total number of tasks assigned to the employee.
    """
    url = "{}/{}/todos".format(base_url, emp_id)
    response = requests.get(url)
    return len(response.json())


def retrieve_completed_tasks(emp_id):
    """
    Retrieves the list of tasks completed by the employee.
    """
    completed_tasks = []
    url = "{}/{}/todos".format(base_url, emp_id)
    response = requests.get(url)
    for task in response.json():
        if task.get("completed"):
            completed_tasks.append(task.get("title"))
    return completed_tasks


def print_employee_progress(emp_name, completed_tasks, assigned_tasks):
    """
    Prints the employee's task list progress.
    """
    print("Employee {} is done with tasks({}/{}):".format(emp_name,
                                                          len(completed_tasks),
                                                          assigned_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    emp_id = sys.argv[1]
    emp_name = retrieve_employee_name(emp_id)
    assigned_tasks = retrieve_assigned_tasks(emp_id)
    completed_tasks = retrieve_completed_tasks(emp_id)
    print_employee_progress(emp_name, completed_tasks, assigned_tasks)
