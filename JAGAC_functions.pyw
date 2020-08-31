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
          SELL_MENU_COMMAND_CHECK(str)


# Open sell menu function
def OPEN_SELL_MENU():
     JAGAC_variables.CAN_RUN_MAIN_COMMANDS = False
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
          print('Closing the sell menu!')
          print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
     ### Sell items
     ## Shiny Gems
     # 1
     if str == '/sell shiny gem 1':
          if JAGAC_variables.resourceSHINY_GEMS > 0:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - 1
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + 20
               print('You sold 1 ✨💎 for 20 🧀')
               print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
               print('and', JAGAC_variables.CHEESE, '🧀')
          else:
               print('You do not have enough Shiny Gems to sell')
     # 10
     if str == '/sell shiny gem 10':
          if JAGAC_variables.resourceSHINY_GEMS > 9:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - 10
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + 200
               print('You sold 10 ✨💎 for 200 🧀')
               print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
               print('and', JAGAC_variables.CHEESE, '🧀')
          else:
               print('You do not have enough Shiny Gems to sell')
     # 100
     if str == '/sell shiny gem 100':
          if JAGAC_variables.resourceSHINY_GEMS > 99:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - 100
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + 2000
               print('You sold 100 ✨💎 for 2000 🧀')
               print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
               print('and', JAGAC_variables.CHEESE, '🧀')
          else:
               print('You do not have enough Shiny Gems to sell')
     # Quarter
     if str == '/sell shiny gem quarter':
          print('You sold', (round(JAGAC_variables.resourceSHINY_GEMS / 4)), '✨💎 for', (round((JAGAC_variables.resourceSHINY_GEMS / 4) * 20)), '🧀')
          JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (round((JAGAC_variables.resourceSHINY_GEMS / 4)) * 20)
          JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - (round(JAGAC_variables.resourceSHINY_GEMS / 4))
          print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          print('and', JAGAC_variables.CHEESE, '🧀')
     # Half
     if str == '/sell shiny gem half':
          print('You sold', (round(JAGAC_variables.resourceSHINY_GEMS / 2)), '✨💎 for', (round((JAGAC_variables.resourceSHINY_GEMS / 2) * 20)), '🧀')
          JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (round((JAGAC_variables.resourceSHINY_GEMS / 2)) * 20)
          JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - (round(JAGAC_variables.resourceSHINY_GEMS / 2))
          print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          print('and', JAGAC_variables.CHEESE, '🧀')
     # All
     if str == '/sell shiny gem all':
          print('You sold', round(JAGAC_variables.resourceSHINY_GEMS), '✨💎 for', round(JAGAC_variables.resourceSHINY_GEMS * 20), '🧀')
          JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + round(JAGAC_variables.resourceSHINY_GEMS * 20)
          JAGAC_variables.resourceSHINY_GEMS = 0
          print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          print('and', JAGAC_variables.CHEESE, '🧀')
     ## Pebbles
     # 1
     if str == '/sell pebble 1':
          if JAGAC_variables.resourceSHINY_GEMS > 0:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - 1
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + 20
               print('You sold 1 ✨💎 for 20 🧀')
               print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
               print('and', JAGAC_variables.CHEESE, '🧀')
          else:
               print('You do not have enough Shiny Gems to sell')
     # 10
     if str == '/sell pebble 10':
          if JAGAC_variables.resourceSHINY_GEMS > 9:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - 10
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + 200
               print('You sold 10 ✨💎 for 200 🧀')
               print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
               print('and', JAGAC_variables.CHEESE, '🧀')
          else:
               print('You do not have enough Shiny Gems to sell')
     # 100
     if str == '/sell pebble 100':
          if JAGAC_variables.resourceSHINY_GEMS > 99:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - 100
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + 2000
               print('You sold 100 ✨💎 for 2000 🧀')
               print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
               print('and', JAGAC_variables.CHEESE, '🧀')
          else:
               print('You do not have enough Shiny Gems to sell')
     # Quarter
     if str == '/sell pebble quarter':
          print('You sold', (round(JAGAC_variables.resourceSHINY_GEMS / 4)), '✨💎 for', (round((JAGAC_variables.resourceSHINY_GEMS / 4) * 20)), '🧀')
          JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (round((JAGAC_variables.resourceSHINY_GEMS / 4)) * 20)
          JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - (round(JAGAC_variables.resourceSHINY_GEMS / 4))
          print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          print('and', JAGAC_variables.CHEESE, '🧀')
     # Half
     if str == '/sell pebble half':
          print('You sold', (round(JAGAC_variables.resourceSHINY_GEMS / 2)), '✨💎 for', (round((JAGAC_variables.resourceSHINY_GEMS / 2) * 20)), '🧀')
          JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (round((JAGAC_variables.resourceSHINY_GEMS / 2)) * 20)
          JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - (round(JAGAC_variables.resourceSHINY_GEMS / 2))
          print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          print('and', JAGAC_variables.CHEESE, '🧀')
     # All
     if str == '/sell pebble all':
          print('You sold', round(JAGAC_variables.resourceSHINY_GEMS), '✨💎 for', round(JAGAC_variables.resourceSHINY_GEMS * 20), '🧀')
          JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + round(JAGAC_variables.resourceSHINY_GEMS * 20)
          JAGAC_variables.resourceSHINY_GEMS = 0
          print('You now have', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          print('and', JAGAC_variables.CHEESE, '🧀')
     return