import ThingsData as td
import utilities
from datetime import datetime
from pywebio.output import put_markdown, put_text


if __name__ == '__main__':

    # Title
    put_markdown('# Welcome')

    # Get requested timeframe
    timeFrame = utilities.askForTimeFrame()

    # Get stats
    stats = td.statsReport(timeFrame)
    createdTasks = stats.getNewTasks()
    completedTasks = stats.getRecentCompletedTasks()
    monthlyCompletions = stats.getMonthlyCompletionRate()

    # Report to standard output
    put_text("""
        In the past %s days you have created %s tasks 
        of which you have completed %s.\n""" %
             (timeFrame, len(createdTasks), len(completedTasks)))
    put_text("\n")

    # Ask if user would like to see all uncompleted tasks
    uncompletedTasks = [i for i in createdTasks if i not in completedTasks]
    utilities.askPrintTasks(uncompletedTasks)

    # Print trends in task completions
    utilities.askPrintTrends(monthlyCompletions)
