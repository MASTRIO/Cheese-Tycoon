import JustAnotherDay_variables
import random

def COMMAND_CHECK(str):
   "Command Input Goes Here!"
   if str == '/help':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is a list of commands:')
        print('/help\n/balance\n/testing add random')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   if str == '/balance':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You have', JustAnotherDay_variables.CHEESE, '🧀 in your wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   if str == '/testing add random':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A random amount of 🧀 has been added to ya wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        JustAnotherDay_variables.CHEESE = JustAnotherDay_variables.CHEESE + random.randint(50,1500)
   return