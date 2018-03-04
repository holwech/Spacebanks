import user
import sqlite3

'''
Check database if the user exist and create new user if not
funding_permission need to be chosen here
'''
<<<<<<< HEAD
def create_funding(status,time_ack, time_expired, funding_type, user_id):
	conn = sqlite3.connect('SQLite_data/funding_storage.db')
	c = conn.cursor()
	funding_count = c.execute('''SELECT count(*) AS "number of fundings"
				FROM user_id
				WHERE user_id = ?''', str(user_id))

	c.execute('''INSERT INTO funding(fundingId, user_id, status, time_ack, time_exp)
				VALUES(?,?,?,?,?)''', (str(funding_count + 1), str(user_id), status, time_ack, time_exp))

	funding_object = user.Funding(status, time_ack, time_expired, funding_type)

	return funding_object
=======

def create_funding(status, time_ack, time_expired, funding_type, userId):

	conn = sqlite3.connect('SQLite_data/funding_storage.db')
	c = conn.cursor()
	c.execute('''SELECT * FROM funding WHERE userId=?''', (str(userId),) )
	user_funding_count = len(c.fetchall())
	c.execute('''INSERT INTO funding(fundingId, userId, status, time_ack, time_exp) VALUES(?,?,?,?,?)''', (str(user_funding_count + 1), str(userId), status, time_ack, time_expired))
	conn.commit()

	funding_object = user.Funding(status, time_ack, time_expired, funding_type)

	return funding_object
>>>>>>> 0044002083fd64c90eb2abb949cfcf9badb9d57e
