import sqlite3
import os


class ThingsData():
    path = os.environ['HOME'] + \
        '/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/Things Database.thingsdatabase/main.sqlite'
    conn = sqlite3.connect(path)

    def getFiveOldestIncompleteTasks(self):
        """
        Prints the 5 oldest, not complete tasks.
        """
        query = "SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title \
            FROM TMTask \
            WHERE status = 0 \
            ORDER BY date \
            LIMIT 5"
        outstandingTasks = self.conn.execute(query).fetchall()
        print("Your oldest outstanding task is from: %s" %
              (outstandingTasks[0][0]))
        for i in outstandingTasks:
            print(i)

    def getTasksPerMonth(self):
        """
        Gets # of tasks per month
        """
        query = "SELECT strftime('%Y-%m', datetime(creationDate, 'unixepoch', 'localtime')) as date, COUNT(*) as n \
                 FROM TMTask \
                 GROUP BY date"
        tasksPerMonth = self.conn.execute(query).fetchall()
        for i in tasksPerMonth:
            print(i)

    def getDescriptiveStats(self):
        """
        Prints lifetime descriptive statistics
        """
        # Uncompleted tasks
        query = "SELECT COUNT(*) \
            FROM TMTask \
            WHERE status = 0"
        uncompletedTasks = self.conn.execute(query).fetchone()

        # Completed Tasks
        query = "SELECT COUNT(*) \
            FROM TMTask \
            WHERE status = 3"
        completedTasks = self.conn.execute(query).fetchone()

        print("You have %s total tasks of which %s are uncompleted." %
              (uncompletedTasks[0] + completedTasks[0], uncompletedTasks[0]))


class statsReport(ThingsData):
    def __init__(self, timeFrame):
        if timeFrame == 'week':
            self.timeFrame = '6'
        elif timeFrame == 'month':
            self.timeFrame = '30'
        else:
            print('Timeframe can either by a week or a month')

    def getNewTasks(self):
        """
        Gets new tasks from the past week.
        """
        query = """
                SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title
                FROM TMTask
                WHERE date BETWEEN datetime('now', '-%s days')
                    AND datetime('now', 'localtime')
                    AND trashed = 0""" % self.timeFrame
        createdTasks = self.conn.execute(query).fetchall()

        return createdTasks

    def getRecentCompletedTasks(self):
        """
        Prints how many tasks were completed in the past week
        """
        query = """
                SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title, status 
                FROM TMTask
                WHERE date BETWEEN datetime('now', '-%s days') AND datetime('now', 'localtime') 
                    AND status = 3
                    AND trashed = 0""" % (self.timeFrame)
        completedTasks = self.conn.execute(query).fetchall()

        return completedTasks
