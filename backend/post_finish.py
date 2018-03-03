'''
update fundings
send finished status
'''
def post_finish(list_of_selected_transactions,funding):
	lost = list_of_selected_transactions
	totalcost = 0
	msg = {'msg': ''}
	for transaction in lost:
		totalcost = totalcost + transaction['amount']


	if totalcost < funding.fundingtype.amount:
		money_back = funding.fundingtype.amount - totalcost
		transfer_money_back_to_business(money_back)
		msg['msg'] = (money_back,' transfered back') #Is dis de way?
	else:
		msg['msg'] = (0,'transfered back')


	funding.status 	= 'finished'
	msg['status'] 	= 'finished'
	return json.dumps(msg)

def transfer_money_back_to_business(amount):
	zero = 0


