from src import ThingsData as td

stats = td.statsReport('month')
stats.getNewTasks()
stats.getRecentCompletedTasks()
