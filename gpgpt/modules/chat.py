from threading import Thread

import sys
import disp
from Crypto.Cipher import AES

#+++++++++++++++++++------________________________
#** D E B U G
#** 1 - ON / 0 - OFF
#-------------------------------------------------
DEBUG_AES = 0
#-------------------------------------------------


""" ********************************************************************    
* Modulo_16_Change
* this function check if the len of text is multiple of 16
* if not then add white gaps to multiple of 16
*       
"""    
def Modulo_16_Change(confidental_data):
    modulo_16 = len(confidental_data)%16
   
    if modulo_16 != 0:
	#print "It is NOT a multiple of 16, adding %d white gaps." % (16-modulo_16)
	confidental_data += ' ' * (16 - len(confidental_data) % 16)
    return confidental_data
   

class write_thread_t(Thread):
  def __init__ (self, client_socket, sec_message):
    Thread.__init__(self)
    self.client_socket = client_socket
    self.sec_message = sec_message

  def run(self):
    secret_key = self.sec_message[-47:-15]
    init_vector = self.sec_message[-16:]
    encryptor = AES.new(secret_key, AES.MODE_CBC, init_vector)
    
    while 1:
      confidental_data = raw_input();
      if 'konec' in confidental_data: 
	self.client_socket.send(encryptor.encrypt(Modulo_16_Change('konec')))
	self.client_socket.close()
	break
      self.client_socket.send(encryptor.encrypt(Modulo_16_Change(confidental_data)))
      
def chat(client_socket, sec_message):
      secret_key = sec_message[-47:-15]
      init_vector = sec_message[-16:]

      wthread = write_thread_t(client_socket, sec_message)
      wthread.start()
      
      encryptor = AES.new(secret_key, AES.MODE_CBC, init_vector)
      while 1:
	data = client_socket.recv(4096)
	if (len(data) != 0):
	  #print('Number of recv char %d' % (len(data)))
	  if 'konec' in data:
		  print "Connection TERMINATE..."
		  self.client_socket.close()
	  else:
	      if len(data) < 4096:
		  enc_sec_msg = data
		  #print "RECEIVED ENCRYPTED MSG: %s" % enc_sec_msg
		  if DEBUG_AES:
                    print "=====CIPHER-TEXT===========IN_HEX==========="
                    disp.split_the_text(enc_sec_msg.encode('hex'), 20)
                    print "=====END-CIPHER-TEXT========================"
		  plain_text = encryptor.decrypt(enc_sec_msg)
		  disp.display(plain_text)
		  
	      else:
		  print "ERROR:", data
