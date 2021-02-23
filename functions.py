# * Import Stuff
import variables as Jvar
import shopMenu as Jshop
import itemAPI as Jitems
import commandSystem as Jcommands

# * Functions
# Commands
def COMMAND_LIST(command):
    # TODO: Make Command List
    Jcommands.chelp(command)
    Jcommands.cversion(command)
    Jcommands.cbalance(command)
    Jcommands.cinventory(command)
    Jcommands.cshop(command)
    Jcommands.csettings(command)
    return

# Items
def ITEM_LIST():
    # TODO: Make Item List
    Jvar.LOADED_RESOURCE_AMOUNT = Jvar.RESOURCES.shiny_gems
    Jitems.newItem("Shiny Gem","✨💎","40","30")
    return