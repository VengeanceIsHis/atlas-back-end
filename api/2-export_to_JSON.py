#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import json
import os
import requests
import sys

if __name__ == "__main__":

    user_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()

    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
