import json
import user as u

def get_fundings(user):
	d = []
	i = 0

	for funding in user.fundings:
		dt = {}

		dt['status'] 					= funding.status
		dt['time_ack'] 					= funding.time_ack
		dt['time_expired'] 				= funding.time_expired
		dt['funding_name'] 				= funding.funding_type.name
		dt['funding_amount'] 			= funding.funding_type.amount
		
		d.append(dt)
		i = i + 1

	return json.dumps(d)


def main():
    FUNDING_TYPE1 = u.Funding_type('Europa 2 dager',500,1,2)
    FUNDING_TYPE2 = u.Funding_type('Trondheim konf',5000,2,2)
    FUNDING_TYPE3 = u.Funding_type('Abu Dhabi er nice',1500,1,5)
    fund1 =  u.Funding('Pending', 1,2, FUNDING_TYPE1,1)
    fund2 =  u.Funding('Approved', 6,7, FUNDING_TYPE3,2)
    user1 = u.User(444,1)
    user1.add_funding(fund1)
    user1.add_funding(fund2)
    fundJson = get_fundings(user1)
    print(json.dumps(fundJson, indent=1))


if __name__ == "__main__":
    main()

