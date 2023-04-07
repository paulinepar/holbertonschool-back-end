#!/usr/bin/python3
'''Write a Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress.
'''
import json
import requests
from sys import argv


if __name__ == '__main__':

    id_user = int(argv[1])

    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    api_url_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id_user}").json()

    EMPLOYEE_NAME = api_url_user['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    for value in api_url_todos:
        if value['userId'] == id_user:
            TOTAL_NUMBER_OF_TASKS += 1
            if value['completed']:
                NUMBER_OF_DONE_TASKS += 1
    print(f'Employee {EMPLOYEE_NAME} is done with'
          f'tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for data in api_url_todos:
        if data['completed'] and data['userId'] == id_user:
            TASK_TITLE = data['title']
            print(f'\t {TASK_TITLE}')
