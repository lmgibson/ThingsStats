import sqlite3
import pandas as pd
import os

path = os.environ['HOME'] + \
    '/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/Things Database.thingsdatabase/main.sqlite'
conn = sqlite3.connect(path)
query = "SELECT datetime(creationDate, 'unixepoch', 'localtime') as date, title, notes , status FROM TMTask"
data = pd.read_sql_query(query, conn)

print(data['status'].value_counts())
