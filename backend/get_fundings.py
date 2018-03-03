import json
import user

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

	return json.dumps(dt)


def main():
    

if __name__ == "__main__":
    main()