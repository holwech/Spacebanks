import requests
import json

ENDPOINT = 'https://dnbapistore.com/hackathon/accounts/3.0/account'
TOKEN = '38d8eddc-8daf-35bc-b582-c3fd3e57798d'
headers = {'Authorization': 'Bearer {}'.format(TOKEN), 'Accept': 'application/json'}

'''
Return a list of transaction in json format or -1 for any error
'''
def get_transactions(user_id,date_start,date_end):

	# Use user_id to get account_number
	r = requests.get(ENDPOINT + '/customer/'+user_id, headers=headers)
	if r.ok:
		accountNumber = r.json()['accounts'][0]['accountNumber']
	else:
		print(r.content)
		return -1

	# Get tranaction list
	param = '?accountNumber='+accountNumber+'&customerId='+user_id+'&dateFrom='+date_start+'&dateTo='+date_end
	r = requests.get(ENDPOINT + param, headers=headers)
	if r.ok:
		transactions = r.json()['transactions']
		return transactions
	else:
		print(r.content)
		return -1


def main():
    transactions = get_transactions('14115374012','2016-01-01','2016-01-05')
    if transactions == -1:
    	print('ERROR: Not able to get tranactions')
    print(transactions)

if __name__ == "__main__":
    main()