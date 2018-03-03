import json
import user as u

def get_fundings(user):
	d = {}
	i = 0

	for funding in user.fundings:
		dt = {}

		dt['status'] 					= funding.status
		dt['time_ack'] 					= funding.time_ack
		dt['time_expired'] 				= funding.time_expired
		dt['funding_name'] 				= funding.funding_type.name
		dt['funding_amount'] 			= funding.funding_type.amount
		
		d[i] = dt
		i = i + 1

	return json.dumps(d)


def main():
    fund1 = u.Funding_type('fund1',500,1,2)
    fund2 = u.Funding_type('fund2',5000,2,2)
    fund3 = u.Funding_type('fund3',1500,1,5)
    user1 = u.User(444,1)
    user1.add_funding(fund1)
    user1.add_funding(fund2)
    user1.add_funding(fund3)
    fundJson = get_fundings(user1)
    print(fundJson)


if __name__ == "__main__":
    main()