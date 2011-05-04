import sys
from termcolor import colored, cprint

def display(print_value):
   cprint(' '+print_value+' ', 'white', 'on_blue')
   return 0
   
def display_input():
   cprint('Insert confidental data :', 'green', 'on_red') 
   return 0
    
    
def split_the_text(text, n):
   i = 1
   #print ('=' * (n*2))
   for c in text:
     print c,
     i+=1
     if i%n == 1:
       print ""
   print ""    
   #print ('=' * (n*2))    
   return 0