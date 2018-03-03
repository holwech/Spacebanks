def handle_request(route, data, funding_types):
	try:
		user_id = data['user_id']
		# user = load the user from db 
		if route == 'user':
			print('create_user()')
			create_user.create_user(user_id)
		elif route == 'getfundings':
			print('get_fundings()')
			get_fundings.get_fundings(user)
		elif route == 'newfunding':
			type_id = data['funding_type']
			print('return_pending()')
			request_funding.return_pending(user, funding_types[type_id])
			print('request_funding()')
			request_funding.request_funding(funding)
		elif route == 'transactions':
			date_start = data['date_start']
			date_end = data['date_end']
			print('get_transactions()')
			get_transactions.get_transactions(user_id,date_start,date_end)
		elif rout == 'finish':
			transactions = data['transactions']
			funding_id = data['funding_id']
			# funding = load from db
			print('post_finish()')
			post_finish.post_finish(transactions,funding)
		else:
			print('Invalid URL')
			return False
		
	except: 
		print('Invalid URL')
		return False

	return True

def request_parser(url):
	try:
		i = url[1:].find('/')
		if i < 0:
			print('Invalid URL')
			return False
		route = url[1:i+1]
		print(route)
		return True
	except:
		print('Invalid URL')
		return False

def main():
	resp = request_parser('/fundings5')
	print(resp)

if __name__ == "__main__":
    main()