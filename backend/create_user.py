import user
import sqlite3

'''
Check database if the user exist and create new user if not
funding_permission need to be chosen here
'''
def create_user(user_id):
    conn = sqlite3.connect('SQLite_data/user_storage.db')
    c = conn.cursor()

    if c.fetchone() == None:
        #fetch user data, and store the new user in database
        c.execute("INSERT INTO users VALUES ('%s','1')" % str(user_id))
        user = user.User(self,user_id, 1 ):
    else:
        user = c.execute('SELECT * FROM users WHERE userid = %s' % str(user_id))

    return user
