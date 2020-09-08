# Import Stuff
import JAGAC_variables
import random
import PySimpleGUI as sg
import time

## Functions
# Command check function
def COMMAND_CHECK(str):
     if JAGAC_variables.CAN_RUN_MAIN_COMMANDS == True:
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
               print('Version', JAGAC_variables.GAME_VERSION)
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
               if JAGAC_variables.resourceBLUE_CHEESE > 0:
                    print('[⭖] Pebbles =', JAGAC_variables.resourcePEBBLE)
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
          # Sell command
          if str == '/sell':
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
               print('Opening Sell Menu!')
               OPEN_SELL_MENU()
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
               JAGAC_variables.resourcePEBBLE = JAGAC_variables.resourcePEBBLE + random.randint(3,150)
          return
     if JAGAC_variables.CAN_RUN_MAIN_COMMANDS == False:
          if JAGAC_variables.CAN_RUN_SELL_COMMANDS == True:
               SELL_MENU_COMMAND_CHECK(str)
          if JAGAC_variables.IS_CHECKING_NUMBERS == True:
               SELL_AMOUNT(str)


# Open sell menu function
def OPEN_SELL_MENU():
     JAGAC_variables.CAN_RUN_MAIN_COMMANDS = False
     JAGAC_variables.CAN_RUN_SELL_COMMANDS = True
     return

# Sell menu command checker
def SELL_MENU_COMMAND_CHECK(str):
     # Sell menu command list
     if str == '/help':
          print('Here is a list of commands for the sell menu:')
          print('> /help\n> /close\n> /sell <item name> <1/10/100/quarter/half/all>\n > /sell?')
     # List of what you can sell
     if str == '/sell?':
          print('Here is a list of what you can sell')
          print('The list is based on what you have')
          if JAGAC_variables.resourceSHINY_GEMS > 0:
               print('> [✨💎] shiny gem')
          if JAGAC_variables.resourceCHEESE_JUMPER > 0:
               print('> [🧀🥋] cheese jumper')
          if JAGAC_variables.resourceBLUE_CHEESE > 0:
               print('> [Ƀ🧀] blue cheese')
          if JAGAC_variables.resourcePEBBLE > 0:
               print('> [⭖] pebble')
     # Close the sell menu
     if str == '/close':
          JAGAC_variables.CAN_RUN_MAIN_COMMANDS = True
          JAGAC_variables.CAN_RUN_SELL_COMMANDS = False
          JAGAC_variables.IS_CHECKING_NUMBERS = False
          print('Closing the sell menu!')
          print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
     ### Sell items
     ## Shiny Gems
     if str == '/sell shiny gem':
          JAGAC_variables.IS_CHECKING_NUMBERS = True
          JAGAC_variables.CAN_RUN_SELL_COMMANDS = False
          JAGAC_variables.RESOURCE_TO_SELL = 'JAGAC_variables.resourceSHINY_GEMS'
          print('How many ✨💎 would you like to sell?')
          print('Max you can sell:', JAGAC_variables.resourceSHINY_GEMS)
     return

def SELL_AMOUNT(int):
     JAGAC_variables.AMOUNT_TO_SELL = int
     if JAGAC_variables.AMOUNT_TO_SELL > JAGAC_variables.RESOURCE_TO_SELL:
          SELL_ALL()
     return

def SELL_ALL():
     print('HA you sold all your', JAGAC_variables.RESOURCE_TO_SELL)
     return