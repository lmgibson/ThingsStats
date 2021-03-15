import ThingsData as td
import utilities
from simple_term_menu import TerminalMenu


if __name__ == '__main__':

    # Get requested timeframe
    timeFrame = utilities.askForTimeFrame()

    # Get stats
    stats = td.statsReport(timeFrame)
    createdTasks = stats.getNewTasks()
    completedTasks = stats.getRecentCompletedTasks()
    monthlyCompletions = stats.getMonthlyCompletionRate()

    # Report to standard output
    print("""
        In the past %s days you have created %s tasks 
        of which you have completed %s.\n""" %
          (timeFrame, len(createdTasks), len(completedTasks)))

    # Ask if user would like to see all created tasks
    utilities.askPrintTasks(createdTasks)

    # Print trends in task completions
    print("\n  Month  Tasks Created   Tasks Completed")
    for dates in monthlyCompletions:
      data = [data for data in dates]
      print("%s:        %s           %s" % (data[0], data[1], data[2]))
