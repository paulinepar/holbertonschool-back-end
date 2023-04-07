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


    user_tasks = []

    for task in api_url_todos:
        if task['userId'] == id_user:
            new_dict = {"task": task['title'],
                         "completed": task['completed'],
                         "username": api_url_user['username']}
            user_tasks.append(new_dict)

    with open(f'{id_user}.json', 'w') as file:
        json.dump({str(id_user): user_tasks}, file)
