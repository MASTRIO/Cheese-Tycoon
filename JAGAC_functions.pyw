# Import Stuff
import JAGAC_variables
import random

## Functions
# Command check function
def COMMAND_CHECK(str):
     if JAGAC_variables.CAN_RUN_MAIN_COMMANDS == True:
          # Help command
          if str == '/help':
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
               print('Here is a list of commands:')
               print('> /help\n> /version\n> /balance\n> /inventory\n> /sell\n> /settings')
               if JAGAC_variables.DEBUG_MODE == True:
                    print('--------------------------------------------------------------------------------------')
                    print('Debug Commands:')
                    print('> /testing add resources')
                    print('> /debug')
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
          # Add random of every resource command
          if str == '/testing add resources':
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
               print('A random amount of every resource has been given to you!')
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + random.randint(50,1500)
               JAGAC_variables.resourceCHEESE_JUMPER = JAGAC_variables.resourceCHEESE_JUMPER + random.randint(3,150)
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS + random.randint(3,150)
               JAGAC_variables.resourceBLUE_CHEESE = JAGAC_variables.resourceBLUE_CHEESE + random.randint(3,150)
               JAGAC_variables.resourcePEBBLE = JAGAC_variables.resourcePEBBLE + random.randint(3,150)
          # Toggle Debug mode
          if str == '/debug':
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
               if JAGAC_variables.DEBUG_MODE == False:
                    JAGAC_variables.DEBUG_MODE = True
                    print('Debug Mode Active')
               elif JAGAC_variables.DEBUG_MODE == True:
                    JAGAC_variables.DEBUG_MODE = False
                    print('Debug Mode Diabl')
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

     if JAGAC_variables.CAN_RUN_MAIN_COMMANDS == False:
          if JAGAC_variables.CAN_RUN_SELL_COMMANDS == True:
               SELL_MENU_COMMAND_CHECK(str)
          if JAGAC_variables.CAN_RUN_BUY_COMMANDS == True:
               BUY_MENU_COMMAND_CHECK(str)
     return


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
          print('> /help\n> /close\n> /sell <item name> <amount>\n > /sell?')
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
     ### Sell item checker
     # Var
     JAGAC_variables.CURRENT_SELL_COMMAND = str
     ## If is
     # Shiny Gem
     JAGAC_variables.SELL_ITEM = JAGAC_variables.CURRENT_SELL_COMMAND.startswith("/sell shiny gem")
     if JAGAC_variables.SELL_ITEM == True:
          SETUP_SELL_DATA()
          if JAGAC_variables.AMOUNT_TO_SELL > JAGAC_variables.resourceSHINY_GEMS:
               print("That number is too high! Plz try again!")
          else:
               JAGAC_variables.resourceSHINY_GEMS = JAGAC_variables.resourceSHINY_GEMS - JAGAC_variables.AMOUNT_TO_SELL
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (JAGAC_variables.AMOUNT_TO_SELL * 40)
               print('You sold', JAGAC_variables.AMOUNT_TO_SELL, '✨💎', 'for', (JAGAC_variables.AMOUNT_TO_SELL * 40))
               print('You now have', JAGAC_variables.CHEESE, '🧀, and', JAGAC_variables.resourceSHINY_GEMS, '✨💎')
          RESET_SELL_DATA()
     # Cheese Jumper
     JAGAC_variables.SELL_ITEM = JAGAC_variables.CURRENT_SELL_COMMAND.startswith("/sell cheese jumper")
     if JAGAC_variables.SELL_ITEM == True:
          SETUP_SELL_DATA()
          if JAGAC_variables.AMOUNT_TO_SELL > JAGAC_variables.resourceCHEESE_JUMPER:
               print("That number is too high! Plz try again!")
          else:
               JAGAC_variables.resourceCHEESE_JUMPER = JAGAC_variables.resourceCHEESE_JUMPER - JAGAC_variables.AMOUNT_TO_SELL
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (JAGAC_variables.AMOUNT_TO_SELL * 90)
               print('You sold', JAGAC_variables.AMOUNT_TO_SELL, '🧀🥋', 'for', (JAGAC_variables.AMOUNT_TO_SELL * 90))
               print('You now have', JAGAC_variables.CHEESE, '🧀, and', JAGAC_variables.resourceCHEESE_JUMPER, '🧀🥋')
          RESET_SELL_DATA()
     # Blue Cheese
     JAGAC_variables.SELL_ITEM = JAGAC_variables.CURRENT_SELL_COMMAND.startswith("/sell blue cheese")
     if JAGAC_variables.SELL_ITEM == True:
          SETUP_SELL_DATA()
          if JAGAC_variables.AMOUNT_TO_SELL > JAGAC_variables.resourceBLUE_CHEESE:
               print("That number is too high! Plz try again!")
          else:
               JAGAC_variables.resourceBLUE_CHEESE = JAGAC_variables.resourceBLUE_CHEESE - JAGAC_variables.AMOUNT_TO_SELL
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (JAGAC_variables.AMOUNT_TO_SELL * 250)
               print('You sold', JAGAC_variables.AMOUNT_TO_SELL, 'Ƀ🧀', 'for', (JAGAC_variables.AMOUNT_TO_SELL * 90))
               print('You now have', JAGAC_variables.CHEESE, '🧀, and', JAGAC_variables.resourceBLUE_CHEESE, 'Ƀ🧀')
          RESET_SELL_DATA()
     # Pebble
     JAGAC_variables.SELL_ITEM = JAGAC_variables.CURRENT_SELL_COMMAND.startswith("/sell pebble")
     if JAGAC_variables.SELL_ITEM == True:
          SETUP_SELL_DATA()
          if JAGAC_variables.AMOUNT_TO_SELL > JAGAC_variables.resourcePEBBLE:
               print("That number is too high! Plz try again!")
          else:
               JAGAC_variables.resourcePEBBLE = JAGAC_variables.resourcePEBBLE - JAGAC_variables.AMOUNT_TO_SELL
               JAGAC_variables.CHEESE = JAGAC_variables.CHEESE + (JAGAC_variables.AMOUNT_TO_SELL * 1)
               print('You sold', JAGAC_variables.AMOUNT_TO_SELL, '⭖', 'for', (JAGAC_variables.AMOUNT_TO_SELL * 90))
               print('You now have', JAGAC_variables.CHEESE, '🧀, and', JAGAC_variables.resourcePEBBLE, '⭖')
          RESET_SELL_DATA()
     return

def SETUP_SELL_DATA():
     JAGAC_variables.AMOUNT_TO_SELL = JAGAC_variables.CURRENT_SELL_COMMAND.strip("/ abcdefghijklmnopqrstuvwxyz")
     JAGAC_variables.AMOUNT_TO_SELL = int(JAGAC_variables.AMOUNT_TO_SELL, base=0)
     return

def RESET_SELL_DATA():
     JAGAC_variables.AMOUNT_TO_SELL = 0
     JAGAC_variables.CURRENT_SELL_COMMAND = 'nothing, yay!'
     return

# Buy menu command check
def BUY_MENU_COMMAND_CHECK(str):
     return