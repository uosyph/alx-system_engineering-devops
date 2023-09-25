#!/usr/bin/python3
"""
Reads info for all employees from an API and saves it to a JSON file
"""

from requests import get
from json import dump



def main():
    """Retrieves data from a REST API for all employees
    and provides an overview of their progress in completing their TODO list.
    Then, saves that data to a JSON file."""

    url_users = "https://jsonplaceholder.typicode.com/users"
    users = get(url_users).json()
    user_dict = {}
    
    for user in users:
        employee_name = user.get("username")
        id = user.get("id")
        url_tasks = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
        tasks = get(url_tasks).json()
        user_list = []
    
        for task in tasks:
            temp_dict = {}
            temp_dict["username"] = employee_name
            temp_dict["task"] = task.get("title")
            temp_dict["completed"] = task.get("completed")
            user_list.append(temp_dict)
    
        user_dict[id] = user_list
    
    with open("todo_all_employees.json", "w") as json_file:
        dump(user_dict, json_file)


if __name__ == "__main__":
    main()
