#!/usr/bin/python3
"""
Reads info for a specified employee from an API and saves it to a JSON file
"""

from sys import argv
from requests import get
from json import dump


def main():
    """Retrieves data from a REST API for a specified employee ID
    and provides an overview of their progress in completing their TODO list.
    Then, saves that data to a JSON file."""

    id = argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_tasks = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    tasks = get(url_tasks).json()
    user_info = get(url_user).json()
    employee_name = user_info.get("username")

    user_list = []
    user_dict = {}

    for task in tasks:
        temp_dict = {}
        temp_dict["task"] = task.get("title")
        temp_dict["completed"] = task.get("completed")
        temp_dict["username"] = employee_name
        user_list.append(temp_dict)

    user_dict[id] = user_list
    with open(f"{id}.json", "w") as json_file:
        dump(user_dict, json_file)


if __name__ == "__main__":
    main()
