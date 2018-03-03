import sqlite3
conn = sqlite3.connect('funding_storage.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE funding
             (fundingId real, userId real, status text, time_ack text, time_exp text)''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()