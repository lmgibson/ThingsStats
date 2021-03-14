from src import ThingsData as td
from src import utilities
import sys


if __name__ == '__main__':

    # Get requested timeframe
    timeFrame = utilities.parseInputs(sys.argv)

    # Get stats
    stats = td.statsReport(timeFrame)
    createdTasks = stats.getNewTasks()
    completedTasks = stats.getRecentCompletedTasks()

    # Report to standard output
    print("""
        In the past %s days you have created %s tasks 
        of which you have completed %s.\n""" %
          (timeFrame, len(createdTasks), len(completedTasks)))

    # Ask if user would like to see all created tasks
    utilities.askPrintTasks(createdTasks)
