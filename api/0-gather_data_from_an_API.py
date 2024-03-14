#!/usr/bin/python3
"""New module based around handlings requests to url"""
import requests

def request(employee_id):
	"""function that defines url and sends request to said url"""
	base_url = "https://jsonplaceholder.typicode.com"
	todo_url = f"{base_url}/todos?userId={employee_id}"

	try:
		# Fetch TODO list for the user
		response = requests.get(todo_url)
		todos = response.json()

		# Check if the user exists
		if not todos:
			print(f"No TODO list found for employee with ID {employee_id}")
			return

        	# Calculate progress
			total_tasks = len(todos)
			completed_tasks = sum(1 for todo in todos if todo['completed'])

			# Print progress information
			print(f"Employee ID: {employee_id}")
			print(f"Total tasks: {total_tasks}")
			print(f"Completed tasks: {completed_tasks}")
			print(f"Progress: {completed_tasks}/{total_tasks} ({(completed_tasks / total_tasks) * 100:.2f}%)")

	except requests.exceptions.RequestException as e:
		print(f"Error fetching TODO list: {e}")