from datetime import date
import sqlite3
import sys
import os

path = os.environ['HOME'] + \
    '/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/Things Database.thingsdatabase/main.sqlite'
conn = sqlite3.connect(path)

# Get date of task by task name
if str.lower(sys.argv[1]) == 'week':
    query = "SELECT strftime('%Y-%m-%d', datetime(creationDate, 'unixepoch', 'localtime')) as date, title, \
            CASE WHEN notes = '' THEN 'No Note' ELSE notes END AS test \
            FROM TMTask \
            WHERE date BETWEEN datetime('now', '-6 days') AND datetime('now', 'localtime') \
            ORDER BY date DESC"
    results = conn.execute(query).fetchall()

    with open((os.environ['HOME'] + '/Desktop/data.txt'), 'w+') as fp:
        fp.write("Created: " + date.today().strftime("%Y-%m-%d") + '\n\n')
        fp.write('\n'.join('%s | %s | %s' % x for x in results))

elif str.lower(sys.argv[1]) == 'month':
    query = "SELECT strftime('%Y-%m-%d', datetime(creationDate, 'unixepoch', 'localtime')) as date, title, \
            CASE WHEN notes = '' THEN 'No Note' ELSE notes END AS test \
            FROM TMTask \
            WHERE date BETWEEN datetime('now', '-30 days') AND datetime('now', 'localtime') \
            ORDER BY date DESC"
    results = conn.execute(query).fetchall()

    with open((os.environ['HOME'] + '/Desktop/data.txt'), 'w+') as fp:
        fp.write("Created: " + date.today().strftime("%Y-%m-%d") + '\n\n')
        fp.write('\n'.join('%s | %s | %s' % x for x in results))

else:
    print("""
    After typing 'python ./getDateData.py' please indicate whether you
    would like data from the past month with 'month' or week with 'week'.

    For example: python ./getDateData.py 'month' will get data from the
    past month.
            """)
