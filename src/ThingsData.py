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
        self.timeFrame = timeFrame

    def getNewTasks(self):
        """Fetches any tasks that were created in the past X days
        but ignores any that are in the trash. 

        Returns:
            list: List of tasks where each item is a tuple of info
            for a given task.
        """
        query = """
                SELECT date(creationDate, 'unixepoch', 'localtime') as date, 
                        title
                FROM TMTask
                WHERE date BETWEEN datetime('now', '-%s days')
                    AND datetime('now', 'localtime')
                    AND trashed = 0
                ORDER BY date DESC""" % (self.timeFrame)
        createdTasks = self.conn.execute(query).fetchall()

        return createdTasks

    def getRecentCompletedTasks(self):
        """Fetches completed tasks that were not trashed in the past
        month or week, depending on user input.

        Returns:
            list: A list of tasks that contain a tuple of information
        """
        query = """
                SELECT date(creationDate, 'unixepoch', 'localtime') as date, 
                       title, status 
                FROM TMTask
                WHERE date BETWEEN datetime('now', '-%s days') AND datetime('now', 'localtime') 
                    AND status = 3
                    AND trashed = 0
                ORDER BY date DESC""" % (self.timeFrame)
        completedTasks = self.conn.execute(query).fetchall()

        return completedTasks

    def getMonthlyCompletionRate(self):
        """Fetches completed tasks that were not trashed in the past
        month or week, depending on user input.

        Returns:
            list: A list of tasks that contain a tuple of information
        """
        query = """
                WITH monthtbl AS (
                    SELECT status,
                            date(date(creationDate, 'unixepoch', 'localtime'),'start of month','+1 month','-1 day') as yrMonth
                    FROM TMTask
                    WHERE trashed = 0
                )
                SELECT strftime('%m-%Y', yrMonth) as newDate,
                       COUNT(yrMonth) as created,
                       SUM(CASE WHEN status = 3 THEN 1
                                ELSE 0 END)
                FROM monthtbl
                GROUP BY yrMonth
                ORDER BY yrMonth DESC
                """
        trends = self.conn.execute(query).fetchall()

        return trends
