import JustAnotherDay_variables
import random

def COMMAND_CHECK(str):
   "Command Input Goes Here!"
   # Help command
   if str == '/help':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is a list of commands:')
        print('/help\n/balance\n/inventory\n/testing add random\n/testing add resources 2')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   # Balance command
   if str == '/balance':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You have', JustAnotherDay_variables.CHEESE, '🧀 in your wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   # Inventory command
   if str == '/inventory':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        if 
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   # Testing add random command
   if str == '/testing add random':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A random amount of 🧀 has been added to ya wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        JustAnotherDay_variables.CHEESE = JustAnotherDay_variables.CHEESE + random.randint(50,1500)
   # Add 2 of every resource command
   if str == '/testing add resources 2':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Two of every resource has been given to you!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        JustAnotherDay_variables.resourceCHEESE_JUMPER = JustAnotherDay_variables.resourceCHEESE_JUMPER + 2
        JustAnotherDay_variables.resourceSHINY_GEMS = JustAnotherDay_variables.resourceSHINY_GEMS + 2
   return