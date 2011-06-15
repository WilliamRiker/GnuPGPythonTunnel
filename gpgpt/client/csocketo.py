#+++++++++++++++++++------________________________
#** C L I E N T  - S E T T I N G S
#-------------------------------------------------
PORT = 5003
SERVER_PUBLIC = '63E685D0'
IP_ADDRESS = 'localhost'

SENDER_NAME = 'BOB'
#-------------------------------------------------

import socket
import commands
import chat
import sys


class App:
  def __init__(self):
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.client_socket.connect((IP_ADDRESS, PORT))

  def Receive_Enc_Aut_Msg(self, DEBUG_MESSAGE):
      data = self.client_socket.recv(4096)
      print('Number of recv char %d' % (len(data)))
      if (len(data) != 0):
	if ( data == 'q' or data == 'Q'):
		self.client_socket.close()
	else:
		if len(data) < 4096:
		    enc_sec_msg = data
		    if DEBUG_MESSAGE:
		      print "RECEIVED ENCRYPTED MSG: %s" % enc_sec_msg
		else:
		    print "ERROR:" , data
	return enc_sec_msg
	
	
  def Send_Encrypted_Msg_To_Server(self, dec_message, DEBUG, DEBUG_NO_CARD):
      if DEBUG_NO_CARD:
	  enc_msg = dec_message
      else:
	  enc_msg = commands.getoutput('echo \'%s\' | gpg --encrypt --armor -r \'%s\'' %(dec_message,SERVER_PUBLIC))
      print "I send message to server"
      self.client_socket.send(enc_msg) 
         
      chat.chat(self.client_socket, dec_message, SENDER_NAME)
      return 0
    
    