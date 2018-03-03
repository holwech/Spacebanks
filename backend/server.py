# -*- coding: utf-8 -*-
import SocketServer
import json
import time
import sys
from datetime import datetime
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""
clientHandlers = {}
msgHistory = []

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def sendMessage(self, message, message_type,sender):
        time_now = str(datetime.now())
        message_dict = {'timestamp':time_now,'sender':sender,'response':message_type,'content':message}
        message_json = json.dumps(message_dict)
        self.connection.sendall(message_json)

    def handleVerifyingUsername(self, suggestedUsername):
        if len(suggestedUsername) == 0:
            return False
        for letter in suggestedUsername:
            asciivalue = ord(letter)
            if not ((asciivalue > 64 and asciivalue <= 90) or (asciivalue >= 97 and asciivalue <= 122) or (asciivalue>47 and asciivalue<=57) ):
                return False

        return True

    def handleUsername(self, received_username_dict):
        #Handling equal usernames
        rcv_username = received_username_dict['content']
        
        while (rcv_username in clientHandlers) or not self.handleVerifyingUsername(rcv_username):
            self.sendMessage('Invalid username, try another username','error','Server')
            received_username_json = self.connection.recv(4096)
            received_username_dict = json.loads(received_username_json)
            rcv_username = received_username_dict['content']
            if rcv_username == None:
                 rcv_username = "."
        return rcv_username


    def handle(self):
        """
        This method handles the connection between a client and the server.
        """

        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request


        while True:
            #Handling client handling in global variable clientHandlers
            received_username_json = self.connection.recv(4096)
            received_username_dict = json.loads(received_username_json)
            if (received_username_dict['request'] == 'login'):
                self.selectedUsername = self.handleUsername(received_username_dict) #assuming usernamedict is pointer handling
                clientHandlers[self.selectedUsername] = self #Add to clientHandlers
                break
            elif (received_username_dict['request'] == 'help'):
                message = 'You are not logged in, these are the available commands \n login \n help \n'
                self.sendMessage(message,'info','Server')
            else:
                message = 'Not a valid command, type help for help \n'
                self.sendMessage(message,'info','Server')

        try:# Loop that listens for messages from the client
            while True:
                received_json = self.connection.recv(4096)
                if (received_json):
                    received_dict = json.loads(received_json)


                    if (received_dict['request'] == 'help'):
                        message = 'These are the available commands \n login \n logout \n names \n history \n'
                        self.sendMessage(message,'info','Server')


                    elif (received_dict['request'] == 'login'):
                        message = 'You are allready logged in'
                        self.sendMessage(message,'info','Server')


                    elif (received_dict['request'] == 'logout'):
                        del clientHandlers[self.selectedUsername]
                        message = 'None'
                        self.sendMessage(message,'logout','Server')


                    elif (received_dict['request'] == 'names'):
                        message = 'The logged on users are: \n'
                        
                        for username in clientHandlers:
                            message += username + '\n'

                        self.sendMessage(message,'info','Server')


                    elif (received_dict['request'] == 'msg'):
                        message = received_dict['content']
                        msgHistory.append(self.selectedUsername + ": " + message)
                        
                        for key in clientHandlers:
                            clientHandlers[key].sendMessage(message,'message',key)

                    elif (received_dict['request'] == 'history'):
                        message = "------------ \n"
                        for msg in msgHistory:
                            message += msg + '\n'
                        self.sendMessage(message,'history','Server')
        except KeyboardInterrupt:
            print "Exit handled"
            sys.exit()

            
    

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()

