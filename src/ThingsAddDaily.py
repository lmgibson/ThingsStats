import webbrowser
from datetime import date, datetime
import things


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
    createDailyToDo()
    addItem()


if __name__ == "__main__":
    addItem()
