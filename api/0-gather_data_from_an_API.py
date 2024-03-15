#!/usr/bin/python3
"""New module based around handlings requests to url"""
import requests
import sys


if __name__ == "__main__":
 url = "https://jsonplaceholder.typicode.com"

 employee_id = sys.argv[1]

 response = requests.get(url + "users/{}".format(employee_id))