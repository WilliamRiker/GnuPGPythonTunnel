# TCP server conf

#+++++++++++++++++++------________________________
#** S E R V E R  - S E T T I N G S
#-------------------------------------------------
PORT = 5003
SENDER_NAME = 'ALICE'
#-------------------------------------------------


import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", PORT))
server_socket.listen(5)

import msgo
import getopt
import sys

#import scryptos
sys.path.append('../modules/')
import chat

def Wait_And_Send_And_Receive_Aut_Msg(enc_sec_message, sec_message, DEBUG, DEBUG_NO_CARD):
    print "TCPServer Waiting for client on port %d" % PORT
    client_socket, address = server_socket.accept()
    print "I got a connection from ", address
    if DEBUG:
      print('I send autentification message. LEN: %d' % (len(enc_sec_message)))
    client_socket.send(enc_sec_message)
    
    print "Wait for recepient message"
    data = client_socket.recv(4096)
    if (len(data) != 0):
	print('Number of recv char %d' % (len(data)))
	#print "DATA RECEIVED: %s" % data
	ret_con_msg = msgo.Confirm_Message(data, sec_message, DEBUG, DEBUG_NO_CARD)
	if ret_con_msg == 111:
	    print "communication error"
	elif ret_con_msg == 1:
	    print "ALL right"
	    chat.chat(client_socket, sec_message, SENDER_NAME);
	else:
	    print "Intruder"
    else:
	print "ERROR, communication FAILED"
	return 0
    return data 
    