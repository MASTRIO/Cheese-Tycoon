###########################################
#                                         #
#        The Shop Menu for JAGAC          #
#                                         #
###########################################

# TODO: Fix This

# * Import
import variables as Jvar
import functions as Jfunc

# * Functions
def chelp(command):
    if command == '/shop':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # Sell
        print('Here is a list of everything you can sell:')
        Jfunc.ITEM_LIST('shop')
        print('-------------------------------------------')
        # Buy
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

def csell(command):
    Jvar.SHOP_COMMAND_STARTING = command.startswith('/sell')
    if Jvar.SHOP_COMMAND_STARTING == True:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        Jvar.SHOP_COMMAND = command
        Jfunc.ITEM_LIST('sell')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

def cbuy(command):
    # TODO: Do this, duh
    return