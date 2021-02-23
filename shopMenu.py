###########################################
#                                         #
#        The Shop Menu for JAGAC          #
#                                         #
###########################################

# TODO: Fix This

# Import
import technicalVariables as techVar

# Open shop menu function
def OPEN_SHOP_MENU():
     techVar.CAN_RUN_MAIN_COMMANDS = False
     techVar.CAN_RUN_SELL_COMMANDS = True
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
          # TODO: Replace with Item API version
          if techVar.resourceSHINY_GEMS > 0:
               print('> [✨💎] shiny gem')
          if techVar.resourceCHEESE_JUMPER > 0:
               print('> [🧀🥋] cheese jumper')
          if techVar.resourceBLUE_CHEESE > 0:
               print('> [Ƀ🧀] blue cheese')
          if techVar.resourcePEBBLE > 0:
               print('> [⭖] pebble')
     # Close the sell menu
     if str == '/close':
          techVar.CAN_RUN_MAIN_COMMANDS = True
          techVar.CAN_RUN_SELL_COMMANDS = False
          techVar.IS_CHECKING_NUMBERS = False
          print('Closing the sell menu!')
          print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')