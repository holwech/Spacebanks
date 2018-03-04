import create_funding
import sqlite3
import json
'''
update fundings
send finished status
'''
def post_finish(list_of_selected_transactions, funding, user_id):
	lost = list_of_selected_transactions
	totalcost = 0
	msg = {'msg': ''}
	for transaction in lost:
		totalcost = totalcost + float(transaction['amount'])


	if totalcost < funding.funding_type.amount:
		money_back = funding.funding_type.amount - totalcost
		transfer_money_back_to_business(money_back)
		msg['msg'] = (money_back,'NOK transfered back') #Is dis de way?
	else:
		msg['msg'] = (0,'NOK transfered back')

	#Update status of funding
	conn = sqlite3.connect('SQLite_data/funding_storage.db')
	c = conn.cursor()
	c.execute('''UPDATE users SET status='finished' WHERE fundingId=%s''', str(user_id))
	conn.commit()
	
	funding.status 	= 'finished'
	msg['status'] 	= 'finished'
	return json.dumps(msg)

def transfer_money_back_to_business(amount):
	zero = 0


