import create_user
import get_fundings
import request_funding
import get_transactions
import post_finish
import get_funding_type

import user as u


def handle_request(route, data, funding_types):
	resp = ""
	try:
		'''
		USED FOR TESTING

		user = u.User(user_id,1)
		FUNDING_TYPE1 = u.Funding_type('Europa 2 dager',500,1,2)
		FUNDING_TYPE2 = u.Funding_type('Trondheim konf',5000,2,2)
		FUNDING_TYPE3 = u.Funding_type('Abu Dhabi er nice',1500,1,5)
		fund1 =  u.Funding('Pending', 1,2, FUNDING_TYPE1)
		fund2 =  u.Funding('Approved', 6,7, FUNDING_TYPE3)
		user.add_funding(fund1)
		user.add_funding(fund2)
		'''
		user_id = data['user_id']
		conn = sqlite3.connect('SQLite_data/funding_storage.db')
		c = conn.cursor()
		user_data = c.execute('''SELECT * FROM funding WHERE userId=?''', (str(user_id),) ).fetchall()
		user = u.User(user_data[userId], user_data['fundingPermission'])

		if route == 'user':
			print('create_user()')
			create_user.create_user(user_id)

		elif route == 'getfundings':
			print('get_fundings()')
			resp = get_fundings.get_fundings(user)

		elif route == 'getfundingtypes':
			resp = get_funding_type.get_fundings_types(funding_types)

		elif route == 'newfunding':
			type_id = data['funding_type']
			print('return_pending()')
			funding = request_funding.return_pending(user, funding_types[type_id])
			print('request_funding()')
			#
			# DB funding = load from db
			#
			resp = request_funding.request_funding(funding)

		elif route == 'transactions':
			date_start = data['date_start']
			date_end = data['date_end']
			print('get_transactions()')
			resp = get_transactions.get_transactions(user_id,date_start,date_end)
			if not resp:
				raise Exception('Not able to fetch transactions')
			elif resp == 450:
				resp = {
	            	'message': 'No Transactions found in the selected period'
	        	}

		elif route == 'finish':
			transactions = data['transactions']
			funding_id = data['funding_id']
			#
			# DB funding = load from db
			#
			print('post_finish()')
			resp = post_finish.post_finish(transactions,funding, user_id)
			#resp = post_finish.post_finish(transactions,fund2, user_id)

		else:
			print('Invalid url')
			return False, resp
		
	except Exception as e: 
		print('Error: ', e)
		return False, resp

	return True, resp

def parser(url):
	try:
		i = url[1:].find('/')
		if i < 0:
			print('Invalid URL')
			return ""
		route = url[1:i+1]
		return route
	except:
		print('Invalid URL')
		return ""

def main():
	resp = parser('/fundings/5')
	print(resp)

if __name__ == "__main__":
    main()