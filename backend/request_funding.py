import json
import time

def request_funding(funding):
	#if user.permission >= funding.funding.permission_type:

	# Wait for 10 sec to simulate that the company is approving the request
	time.sleep(10) 

	if 1:
		transfer_money()
		funding.status = 'approved'

	else:
		funding.status = 'denied'
	
	msg = {'status':funding.status}
	return json.dumps(msg)

def return_pending(user, funding):
	# Save status to db
	funding.status = 'pending'
	msg = {'status':funding.status}
	user.add_funding(funding)

	return json.dumps(msg)

def transfer_money():
	one = 1