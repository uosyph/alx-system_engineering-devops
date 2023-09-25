#!/usr/bin/python3
"""
Reads info for a specified employee from an API and prints it out
"""

from sys import argv
from requests import get


def main():
    """Retrieves data from a REST API for a specified employee ID
    and provides an overview of their progress in completing their TODO list.
    Then, prints out that data."""

    id = argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_tasks = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
    
    res = get(url_tasks)
    tasks = res.json()
    
    user_info = get(url_user).json()
    employee_name = user_info["name"]
    done_tasks = [task for task in tasks if task["completed"]]
    
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), len(tasks)
        )
    )
    
    for task in done_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    main()
