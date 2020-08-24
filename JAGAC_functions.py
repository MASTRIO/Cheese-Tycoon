# Import Stuff
import JAGAC_variables
import random
import PySimpleGUI as sg
import time

# Variables
GameVersion = 'v0.1'

# Command check function
def COMMAND_CHECK(str):
   "Command Input Goes Here!"
   # Help command
   if str == '/help':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is a list of commands:')
        print('> /help\n> /version\n> /balance\n> /inventory\n> /sell\n> /settings')
        print('--------------------------------------------------------------------------------------')
        print('Testing/Temporary Commands:')
        print('> /testing add resources')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   # Version command
   if str == '/version':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('JAGAC:')
        print('Version', GameVersion)
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
   # Sell command
   if str == '/sell':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Opening Sell Menu!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        layout2 = [[sg.Text('Welcome to the sell menu!')],
                  ]

        window2 = sg.Window('JAGAC - Sell Menu', layout2, location=(450, 115), return_keyboard_events=True)

        while True:
               event, values = window2.read()
               # Runs when CLOSE is pressed
               if event in (sg.WIN_CLOSED,):
                    time.sleep(0.5)
                    window2.close()
   # Settings command
   if str == '/settings':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Opening Settings Menu!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
## Testing Commands
   # Add 2 of every resource command
   if str == '/testing add resources':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('A random amount of every resource has been given to you!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + random.randint(50,1500)
        JAGAC_variables.resourceCHEESE_JUMPER = JAGAC_variables.resourceCHEESE_JUMPER + random.randint(3,150)
        JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS + random.randint(3,150)
        JAGAC_variables.resourceBLUE_CHEESE = JAGAC_variables.resourceBLUE_CHEESE + random.randint(3,150)
   return