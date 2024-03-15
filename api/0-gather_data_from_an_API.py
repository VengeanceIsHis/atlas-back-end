#!/usr/bin/python3
"""New module based around handlings requests to url"""
import requests
import sys


if __name__ == "__main__":
 url = "https://jsonplaceholder.typicode.com"

 employee_id = sys.argv[1]

 response = requests.get(url + "users/{}".format(employee_id))

 user = response.json()

 param = {"user.id": employee_id}

 todos = requests.get(url + "todos", params=param)

 todo = todos.json()

 complete = []

 for todo in todos:
  if todo.get("completed") is True:
   complete.append(todo.get("title"))

 print("Employee {} is done with tasks({}/{})".format(user.get("name"), len(complete), len(todos)))