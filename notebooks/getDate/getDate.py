import sqlite3
import sys
import os

path = os.environ['HOME'] + \
    '/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/Things Database.thingsdatabase/main.sqlite'

conn = sqlite3.connect(path)

# Get date of task by task name
query = "SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title, status \
    FROM TMTask \
    WHERE title LIKE '%%%s%%';" % sys.argv[1]
results = conn.execute(query).fetchall()

# Print line by line
for i in results:
    print("Title: %s. Date Created: %s." % (i[1], i[0]))
