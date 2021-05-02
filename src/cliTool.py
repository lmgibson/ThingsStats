from typing import Counter
import things
import utilities
from datetime import datetime
from PyInquirer import prompt


if __name__ == "__main__":
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
                    Stats Overview
    ================================================
    In the past %s days you have created 
    %s tasks of which you have completed %s.
            """ % (timeFrame,
                   totalTaskCount,
                   len(completedTasks))

    print(report)
