#!/usr/bin/python3
'''Write a Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress.
'''
import json
import requests
from sys import argv


if __name__ == '__main__':

    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/").json()

    api_url_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/").json()
    
    user_tasks = []
    json_file = {}

    for user in api_url_user:
        user_id = user["id"]
        username = user["username"]
        user_tasks = []
        for task in api_url_todos:
            if task['userId'] == user['id']:
                new_dict = {"username": username,
                            "task": task['title'],
                            "completed": task['completed']}
                user_tasks.append(new_dict)
        json_file[user_id] = user_tasks

    print(json_file)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(json_file, file)
    '''
    user_tasks = []

    for task in api_url_todos:
        if task['userId'] == api_url_todos:
            new_dict = {"username": api_url_user['username'],
                        "task": task['title'],
                        "completed": task['completed']}
            user_tasks.append(new_dict)

    with open('todo_all_employees.json', 'w') as file:
        json.dump({str(api_url_todos): user_tasks}, file)'''
