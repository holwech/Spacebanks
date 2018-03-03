import user
import sqlite3

'''
Check database if the user exist and create new user if not
funding_permission need to be chosen here
'''

def create_funding(status, time_ack, time_expired, funding_type, userId):

	conn = sqlite3.connect('SQLite_data/funding_storage.db')
	c = conn.cursor()
	c.execute('''SELECT * FROM funding WHERE userId=?''', (str(userId),) )
	user_funding_count = len(c.fetchall())
	c.execute('''INSERT INTO funding(fundingId, userId, status, time_ack, time_exp) VALUES(?,?,?,?,?)''', (str(user_funding_count + 1), str(userId), status, time_ack, time_expired))
	conn.commit()

	funding_object = user.Funding(status, time_ack, time_expired, funding_type)

	return funding_object
