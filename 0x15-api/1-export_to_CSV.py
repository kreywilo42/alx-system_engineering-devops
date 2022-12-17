#!/usr/bin/python3
"""returns information about an employee's todo list progress"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    user = requests.get(url + "{}".format(argv[1])).json()
    todos = requests.get(url + "{}/todos".format(argv[1])).json()

    with open("{}.csv".format(user.get('id')), "w+") as f:
        file = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            file.writerow([user.get('id'), user.get('username'),
                          todo.get('completed'), todo.get('title')])
