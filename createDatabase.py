import sqlite3
import pandas as pd


conn = sqlite3.connect('TheBats.db')
c = conn.cursor()

# Create table
c.execute('CREATE TABLE batquote (id INTEGER PRIMARY KEY, message text)')

# Insert a row of data
c.execute("INSERT INTO batquote (message) VALUES ('i batman')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()


print(pd.read_sql_query('SELECT * FROM batquote', conn))