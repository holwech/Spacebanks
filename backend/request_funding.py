import json

def request_funding(user,funding):
	#if user.permission >= funding.funding.oermission_type:
	if 1:
		transfer_money()
		funding.status = 'accepted'

	else:
		funding.status = 'denied'
	user.add_funding(funding)

	msg = {'status':funding.status}
	return json.dumps(msg)

def return_pending(funding):
	#d for dict
	funding.status = 'pending'
	msg = {'status':funding.status}
	#d['status'] = 'pending'
#	user.status = 'pending'

	return json.dumps(msg)

def transfer_money():
	t = 1