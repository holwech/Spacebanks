import json

def get_fundings_type():
	d = [
	{	'name': 'Europa 2 dager',
		'amount': 500,
		'permission_type': 1,
		'duration': 2
		},
	{	'name': 'Trondheim konf',
		'amount': 1500,
		'permission_type': 1,
		'duration': 1
		},
	{	'name': 'Abu Dhabi ferie',
		'amount': 50000,
		'permission_type': 2,
		'duration': 5
		}
	]

	return json.dumps(d)
