#!/usr/bin/python3
import json
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import request_handler as handler
import codecs

ENDPOINT = 'https://dnbapistore.com/hackathon/customers/3.0'
TOKEN = '38d8eddc-8daf-35bc-b582-c3fd3e57798d'
headers = {'Authorization': 'Bearer {}'.format(TOKEN), 'Accept': 'application/json'}


hostName = ''
hostPort = 5555

# Create a some fundingTypes used for DEMO
#FUNDING_TYPE = u.Funding_type('Europa 2 dager',500,1,2)
FUNDING_TYPES = [
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


class httpServer(BaseHTTPRequestHandler):

	def _set_response(self, code):
		self.send_response(code)
		self.send_header('Content-type', 'application/json')
		self.end_headers()

	#	GET
	def do_GET(self):

		# Parse request 
		route = handler.parser(self.path)

		# Handle request
		if route == '':
			print('Invalid request')
			request_is_valid = False
		else:
			content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
			post_data = self.rfile.read(content_length)			 # <--- Gets the data itself
			reader = codecs.getreader("utf-8")
			data = json.loads(reader(post_data))
			request_is_valid, resp = handler.handle_request(route, data, FUNDING_TYPES)


		# Send response
		if request_is_valid:
			print('response: ', resp)
			self._set_response(200)
			if resp:
				self.wfile.write(resp.encode())
		else:
			# Create response
			print('Invalid request, error in handle_request')
			self._set_response(404)
			self.wfile.write(json.dumps({
	            'Error': 'Invalid request'
	        }).encode())

	#	POST 
	def do_POST(self):

		# Parse request 
		route = handler.parser(self.path)

		# Handle request
		if route == '':
			print('Invalid request')
			request_is_valid = False
		else:
			content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
			post_data = self.rfile.read(content_length)			 # <--- Gets the data itself
			data = json.loads(post_data)
			request_is_valid, resp = handler.handle_request(route, data, FUNDING_TYPES)


		# Send response
		if request_is_valid:
			print('response: ', resp)
			self._set_response(200)
			self.wfile.write(resp.encode())
		else:
			# Create response
			print('Invalid request, error in handle_request')
			self._set_response(404)
			self.wfile.write(json.dumps({
	            'Error': 'Invalid request'
	        }).encode())
				
		



server = HTTPServer((hostName, hostPort), httpServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	server.serve_forever()
except KeyboardInterrupt:
	pass

server.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

