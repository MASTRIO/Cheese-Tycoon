###########################################
#                                         #
#      The Command System for JAGAC       #
#                                         #
###########################################

# * Imports
import variables as Jvar
import functions as Jfunc
import shop as Jshop

# * Commands
# Help
def chelp(command):
    if command == '/help':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is a list of commands:')
        print('> /help\n> /version\n> /balance\n> /inventory\n> /sell\n> /settings')
        if Jvar.DEBUG_MODE == True:
            print('--------------------------------------------------------------------------------------')
            print('Debug Commands:')
            print('> /testing add resources')
            print('> /debug')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

# Version
def cversion(command):
    if command == '/version':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('JAGAC:')
        print('Version', Jvar.GAME_VERSION)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

# Balance
def cbalance(command):
    if command == '/balance':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You have', Jvar.CHEESE, '🧀 in your wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

# Inventory
def cinventory(command):
    if command == '/inventory':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is everything in your inventory:')
        Jfunc.ITEM_LIST('inventory')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

# Settings
def csettings(command):
    if command == '/settings':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('test')
        print('Opening Settings Menu!')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return