from src import ThingsData as td
import sys


if sys.argv[1] in ['month', 'week']:
    timeFrame = sys.argv[1]
else:
    print("Please provide a timeframe of 'month' or 'week'")
    exit()

stats = td.statsReport(timeFrame)
createdTasks = stats.getNewTasks()
completedTasks = stats.getRecentCompletedTasks()

print("""
    In the past %s you have created %s tasks 
    of which you have completed %s.\n""" %
      (timeFrame, len(createdTasks), len(completedTasks)))

for i in createdTasks:
    print(i)
