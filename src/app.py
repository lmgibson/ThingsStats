from typing import Counter
import things
import utilities
from datetime import datetime
from pywebio import start_server
from pywebio.output import put_markdown


def main():
    # Title
    put_markdown('# Welcome')

    # Get requested timeframe
    timeFrame = utilities.askForTimeFrame()

    # Get stats
    totalTaskCount = things.tasks(last=timeFrame, status=None,
                                  trashed=False, type='to-do', count_only=True)
    completedTasks = things.tasks(
        last=timeFrame, status='completed', type='to-do')
    incompleteTasks = things.tasks(
        last=timeFrame, status='incomplete', type='to-do')

    # Report to standard output
    put_markdown("""### Stats Overview
        In the past %s days you have created %s tasks of which you have completed %s.
        """ %
                 (timeFrame, totalTaskCount, len(completedTasks)), lstrip=True)

    # Ask if user would like to see all uncompleted tasks
    utilities.askPrintTasks(incompleteTasks)

    # Print trends in task completions
    utilities.askPrintTrends()


if __name__ == '__main__':
    main()
