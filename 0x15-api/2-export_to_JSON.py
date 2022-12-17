#!/usr/bin/python3
"""returns information about an employee's todo list progress"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(url + "{}".format(argv[1])).json()
    todos = requests.get(url + "{}/todos".format(argv[1])).json()

    with open("{}.json".format(user.get('id')), "w+") as f:
        json.dump({user.get('id'): [{
                  "task": todo.get('title'),
                  "completed": todo.get('completed'),
                  "username": user.get('username')}
                  for todo in todos]
                  }, f)
