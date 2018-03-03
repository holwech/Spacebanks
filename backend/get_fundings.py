import json
def get_fundings(user):
	d = {}
	i = 0
	for funding in user.fundings:

		funding_name = 'funding'+i
		dt = {}

		dt['status'] 					= funding.status
		dt['time_ack'] 					= funding.time_ack
		dt['time_expired'] 				= funding.time_expired
		dt['funding_name'] 				= funding.funding_type.name
		dt['funding_amount'] 			= funding.funding_type.amount
		dt['funding_permission_type'] 	= funding.funding_type.permission_type
		
		d[funding_name] = dt
		i = i + 1

	return json.dumps(dt)


