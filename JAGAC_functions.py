import JAGAC_variables
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
        print('You have', JAGAC_variables.CHEESE, '🧀 in your wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   # Inventory command
   if str == '/inventory':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is everything in your inventory:')
        if JAGAC_variables.resourceSHINY_GEMS > 0:
             print('[✨💎] Shiny Gems =', JAGAC_variables.resourceSHINY_GEMS)
        if JAGAC_variables.resourceCHEESE_JUMPER > 0:
             print('[🧀🥋] Cheese Jumpers =', JAGAC_variables.resourceCHEESE_JUMPER)
        if JAGAC_variables.resourceBLUE_CHEESE > 0:
             print('[Ƀ🧀] Blue Cheese =', JAGAC_variables.resourceBLUE_CHEESE)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   # Testing add random command
   if str == '/testing add random':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A random amount of 🧀 has been added to ya wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + random.randint(50,1500)
   # Add 2 of every resource command
   if str == '/testing add resources':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A random amount of every resource has been given to you!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        JAGAC_variables.resourceCHEESE_JUMPER = JAGAC_variables.resourceCHEESE_JUMPER + random.randint(3,150)
        JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS + random.randint(3,150)
        JAGAC_variables.resourceBLUE_CHEESE = JAGAC_variables.resourceBLUE_CHEESE + random.randint(3,150)
   return