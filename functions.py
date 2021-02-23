# * Import Stuff
import variables as Jvar
import shopMenu as Jshop
import itemAPI as Jitems
import commandSystem as Jcommands
import resources as Jres

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
def ITEM_LIST(access):
    # TODO: Make Item List
    Jvar.LOADED_RESOURCE_AMOUNT = Jres.shiny_gems
    Jitems.newItem(access,'Shiny Gem','✨💎',40,30)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.cheese_jumpers
    Jitems.newItem(access,'Cheese Jumper','🧀🥋',90,100)
    return