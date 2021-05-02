from typing import Counter
import things
import utilities
from datetime import datetime


def test():
    input("What is your name")


def main():
    # Title
    put_markdown('# Welcome')

    # Get requested timeframe
    timeFrame = utilities.askForTimeFrame()

    # Get stats
    totalTaskCount = things.todos(last=timeFrame, status=None,
                                  trashed=False, count_only=True)
    completedTasks = things.todos(
        last=timeFrame, status='completed')
    incompleteTasks = things.todos(
        last=timeFrame, status='incomplete')

    # Report to standard output
    put_markdown("""### Stats Overview
        In the past %s days you have created %s tasks of which you have completed %s.
        """ %
                 (timeFrame, totalTaskCount, len(completedTasks)), lstrip=True)

    # Ask if user would like to see all uncompleted tasks
    utilities.askPrintTasks(incompleteTasks)

    # Print trends in task completions
    utilities.askPrintTrends()


if __name__ == "__main__":
    main()
