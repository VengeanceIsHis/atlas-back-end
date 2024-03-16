#!/usr/bin/python3
import sys
from employee_todo_progress import fetch_employee_todo_progress

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)