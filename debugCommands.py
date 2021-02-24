###########################################
#                                         #
#   The Debug Command System for JAGAC    #
#                                         #
###########################################

# * Imports
import variables as Jvar
import functions as Jfunc
import resources as Jres

# Settings
def cdebug(command):
    if command == '/debug':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        # Enable Debug Mode
        if Jvar.DEBUG_MODE == False:
            Jvar.DEBUG_MODE = True
            print('Debug Mode Enabled')
        # Disable Debug Mode
        elif Jvar.DEBUG_MODE == True:
            Jvar.DEBUG_MODE = False
            print('Debug Mode Disabled')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    return

# Add Resources
def caddResources(command):
    Jvar.DEBUG_CONTAINS = command.startswith('/debug resources')
    if Jvar.DEBUG_CONTAINS == True:
        # Strip the string and convert to int
        Jvar.DEBUG_INCREASE = command.strip('/ abcdefghijklmnopqrstuvwxyz')
        Jvar.DEBUG_INCREASE = int(command, base=0)

        # Increase the resources
        Jfunc.ITEM_LIST('DEBUG.increaseResources')
        Jres.CHEESE = Jres.CHEESE +  + Jvar.DEBUG_INCREASE

        # Print
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Increased resources for all items by {}'.format(Jvar.DEBUG_INCREASE))
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    return