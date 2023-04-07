#!/usr/bin/python3
'''Write a Python script that, using this REST API, for a given employee ID,
   returns information about his/her TODO list progress.
'''
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':

    id_user = int(argv[1])

    api_url_todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId=2").json()

    api_url_user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{id_user}").json()

    EMPLOYEE_NAME = api_url_user['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    with open(f'{id_user}.csv', 'wt') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in api_url_todos:
            List = []
            List.append(i['userId'])
            List.append(api_url_user['username'])
            List.append(i['completed'])
            List.append(i['title'])

            writer.writerow(List)
        file.close()
