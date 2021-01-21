import sqlite3
import os

path = os.environ['HOME'] + \
    '/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/Things Database.thingsdatabase/main.sqlite'
conn = sqlite3.connect(path)


# Get Tasks set in the past week
query = "SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title, status \
    FROM TMTask \
    WHERE date BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime')"
pastWeek = conn.execute(query).fetchall()
print("In the past week you have created %s new tasks:" % (len(pastWeek)))
for i in pastWeek:
    print(i)


# Get Descriptive Statistics
# Uncompleted tasks
query = "SELECT COUNT(*) \
    FROM TMTask \
    WHERE status = 0"
uncompletedTasks = conn.execute(query).fetchone()

# Completed Tasks
query = "SELECT COUNT(*) \
    FROM TMTask \
    WHERE status = 3"
completedTasks = conn.execute(query).fetchone()

print("You have %s total tasks of which %s are uncompleted." %
      (uncompletedTasks[0] + completedTasks[0], uncompletedTasks[0]))


# Get top 5 most outstanding tasks
query = "SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title, status \
    FROM TMTask \
    WHERE status = 0 \
    ORDER BY date \
    LIMIT 5"
outstandingTasks = conn.execute(query).fetchall()
print("Your oldest outstanding task is from: %s" % (outstandingTasks[0][0]))
for i in outstandingTasks:
    print(i)
