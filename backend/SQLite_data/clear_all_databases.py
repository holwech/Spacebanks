import sqlite3

conn1 = sqlite3.connect('user_storage.db')
c1 = conn1.cursor()
c1.execute('DELETE FROM users')
conn1.commit()

conn2 = sqlite3.connect('funding_storage.db')
c2 = conn2.cursor()
c2.execute('DELETE FROM funding')
conn2.commit()

