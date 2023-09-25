#!/usr/bin/python3
"""
Reads info for a specified employee from an API and saves it to a CSV file
"""

from sys import argv
from requests import get
import csv


def main():
    """Retrieves data from a REST API for a specified employee ID
    and provides an overview of their progress in completing their TODO list.
    Then, saves that data to a CSV file."""

    id = argv[1]
    url_user = f"https://jsonplaceholder.typicode.com/users/{id}"
    url_tasks = f"https://jsonplaceholder.typicode.com/users/{id}/todos"

    tasks = get(url_tasks).json()
    user_info = get(url_user).json()
    employee_name = user_info.get("username")

    with open(f"{id}.csv", "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                [
                    task.get("userId"),
                    employee_name,
                    task.get("completed"),
                    task.get("title"),
                ]
            )


if __name__ == "__main__":
    main()
