import json
import time
import create_funding as cf
import user as u

def request_funding(funding):
	# Wait for 10 sec to simulate that the company is approving the request
	time.sleep(10) 

	#if user.permission >= funding.funding.permission_type:
	if 1:
		transfer_money()
		funding.status = 'approved'

	else:
		funding.status = 'denied'
	
	# Save status to db
	msg = {'status':funding.status}
	return json.dumps(msg)

def return_pending(user, funding_type):
	dayStr = time.strftime("%Y-%m-%d")
	day = int(dayStr[(len(dayStr)-2):len(dayStr)]) + funding_type.duration
	time_expired = dayStr[0:(len(dayStr)-1)] + str(day)
	print(time_expired)
	#funding = u.Funding('pending',time.strftime("%Y-%m-%d"),time_expired,funding_type)
	funding = cf.create_funding('pending', time.strftime("%Y-%m-%d"), time_expired, funding_type, user.userId)

	msg = {'status':funding.status}
	user.add_funding(funding)

	return funding


def transfer_money():
	one = 1


def main():
	FUNDING_TYPE1 = u.Funding_type('Europa 2 dager',500,1,2)
	user1 = u.User(444,1)
	fundJson = return_pending(user1, FUNDING_TYPE1)
	print(json.dumps(fundJson, indent=1))

if __name__ == "__main__":
    main()