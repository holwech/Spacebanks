import user
import sqlite3

'''
Check database if the user exist and create new user if not
funding_permission need to be chosen here
'''
def create_user(user_id):
    conn = sqlite3.connect('SQLite_data/user_storage.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users WHERE userId=?''', (user_id,))
    user_data = c.fetchone()

    if user_data == None:
        #Add uset to database, and store the new user in database
        c.execute('''INSERT INTO users(userId, fundingPermission)
                  VALUES(?,?)''', (str(user_id), 1))
        return_user = user.User(user_id, 1)
        conn.commit()
    else:
        #Fetch user from database
        return_user = user.User(user_id, 1) #Should eventually fetch user data

    return return_user