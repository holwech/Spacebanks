#!/usr/bin/python3
import json

import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

ENDPOINT = 'https://dnbapistore.com/hackathon/customers/3.0'
TOKEN = '38d8eddc-8daf-35bc-b582-c3fd3e57798d'
headers = {'Authorization': 'Bearer {}'.format(TOKEN), 'Accept': 'application/json'}


hostName = ''
hostPort = 5555

# Create a some fundingTypes used for DEMO
FUNDING_TYPE1 = u.Funding_type('Europa 2 dager',500,1,2)
FUNDING_TYPE2 = u.Funding_type('Trondheim konf',5000,2,2)
FUNDING_TYPE3 = u.Funding_type('Abu Dhabi er nice',1500,1,5)

class httpServer(BaseHTTPRequestHandler):

	def _set_response(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	#	GET
	def do_GET(self):

		# Parse request

		# Handle request


		# Create response
		self._set_response()
		self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

	#	POST 
	def do_POST(self):

		# Parse request 

		# Handle request

		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) 		 # <--- Gets the data itself

		# Create response
		self._set_response()
		self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))



server = HTTPServer((hostName, hostPort), httpServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	server.serve_forever()
except KeyboardInterrupt:
	pass

server.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

