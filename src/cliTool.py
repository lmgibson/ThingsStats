from typing import Counter
import things
import utilities
from datetime import datetime
from PyInquirer import prompt
from rich.console import Console
from rich.table import Table


def main():
    console = Console()

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
    report = """
          :raccoon: Stats Overview :raccoon: 
    ------------------------------------
    In the past %s days you have [bold]created[/bold] 
    %s tasks of which you have [bold]completed[/bold] %s.
    """ % (timeFrame[:-1],
           totalTaskCount,
           len(completedTasks))

    console.print(report)

    # Ask if user would like to see all uncompleted tasks
    utilities.askPrintTasks(incompleteTasks, console)

    # Print trends in task completions
    utilities.askPrintTrends(console)

    # Ask if they would like to explore another date (loops back to start)
    utilities.askStartAgain()


if __name__ == "__main__":
    main()
