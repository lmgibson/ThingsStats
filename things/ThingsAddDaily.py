import webbrowser
from datetime import date, datetime


def createDailyToDo():
    today = datetime.now().date()
    weekday = today.strftime('%A')
    formattedDate = f"{weekday} {today.month}/{today.day}/{today.year}"

    url = f"things:///add?title={formattedDate}&list=Daily Tracker"
    success = webbrowser.open(url)
    if success:
        print("Created new todo for today")


def addItem():
    today = datetime.now().date()
    weekday = today.strftime('%A')
    formattedDate = f"{weekday} {today.month}/{today.day}/{today.year}"

    url = f"things:///update?"


def main():
    title = input("What would you like to add")
    project = "Daily Tracker"
    url = f"things:///add?title={title}&list={project}"
    webbrowser.open(url)


if __name__ == "__main__":
    createDailyToDo()
