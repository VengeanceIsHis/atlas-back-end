#!/usr/bin/python3
"""New module based around handlings requests to url"""
import requests


def request(employee_id):
    """function that defines url and sends request to said url"""
    def get_todo_progress(employee_id):
        base_url = "https://jsonplaceholder.typicode.com"
        todo_url = f"{base_url}/todos?userId={employee_id}"

        try:
            response = requests.get(todo_url)
            todos = response.json()

            if not todos:
                print(f"No TODO list found for employee with ID {employee_id}")
                return

            # Get employee name
            user_url = f"{base_url}/users/{employee_id}"
            user_response = requests.get(user_url)
            employee_name = user_response.json()['name']

            completed_tasks = []
            for todo in todos:
                if todo['completed']:
                    completed_tasks.append(todo['title'])

            total_tasks = len(todos)
            num_completed_tasks = len(completed_tasks)

            print(f"{employee_name}:")
            for task_title in completed_tasks:
                print(f"\t{task_title}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching TODO list: {e}")
