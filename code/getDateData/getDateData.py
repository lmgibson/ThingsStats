from datetime import date
import sqlite3
import sys
import os

path = os.environ['HOME'] + \
    '/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/Things Database.thingsdatabase/main.sqlite'
conn = sqlite3.connect(path)
dateCreated = "Created: %s \n\n" % date.today().strftime("%Y-%m-%d")

# Converting argument to numeric value
if str.lower(sys.argv[1]) == 'week':
    timeFrame = 7
elif str.lower(sys.argv[1]) == 'month':
    timeFrame = 30
else:
    print("""
    After typing 'python ./getDateData.py' please indicate whether you
    would like data from the past month with 'month' or week with 'week'.

    For example: python ./getDateData.py 'month' will get data from the
    past month.
            """)
    quit()

# Get data for past week or month and save out to a file.
query = "SELECT strftime('%%Y-%%m-%%d', datetime(creationDate, 'unixepoch', 'localtime')) as date, title \
        FROM TMTask \
        WHERE date BETWEEN datetime('now', '-%s days') AND datetime('now', 'localtime') \
        ORDER BY date DESC" % timeFrame
results = conn.execute(query).fetchall()

with open((os.environ['HOME'] + '/Desktop/' + date.today().strftime("%Y-%m-%d") + '_ThingsData.txt'), 'w+') as fp:
    fp.write(dateCreated)
    for val in results:
        fp.write(('\n %s %s' %
                  (val[0].encode('utf-8-sig'), val[1].encode('utf-8'))))
