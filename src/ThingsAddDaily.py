import webbrowser
from datetime import datetime
import things
import os


def getListOfTodos():
    activeTodos = [i['title']
                   for i in things.todos() if i['project_title'] == 'Daily Tracker']

    return activeTodos


def getID(formattedDate):
    id = [i['uuid'] for i in things.todos() if i['title'] == formattedDate]


def addChecklistItem(activeTodos, message):
    # Construct todo name
    today = datetime.now().date()
    weekday = today.strftime('%A')
    formattedDate = f"{weekday} {today.month}/{today.day}/{today.year}"

    # Check if todo exists, if not create it
    if formattedDate not in activeTodos:
        url = f"things:///add?title={formattedDate}&list=Daily Tracker"
        success = webbrowser.open(url)
        if success:
            print("Created new todo for today")

    # Add item
    id = [i['uuid'] for i in things.todos() if i['title'] == formattedDate]
    message = message
    token = os.environ['THINGS_TOKEN']
    url = f"things:///update?id={id}&auth-token={token}&append-checklist-items={message}"
    webbrowser.open(url)


def main(message):
    activeTodos = getListOfTodos()
    addChecklistItem(activeTodos, message)


if __name__ == "__main__":
    main()
