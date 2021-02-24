###########################################
#                                         #
#       The Function List for JAGAC       #
#                                         #
###########################################

# * Import Stuff
import variables as Jvar
import itemAPI as Jitems
import commandSystem as Jcommands
import debugCommands as Dcommands
import resources as Jres

# * Functions
# Commands
def COMMAND_LIST(command):
    # Normal Commands
    Jcommands.chelp(command)
    Jcommands.cversion(command)
    Jcommands.cbalance(command)
    Jcommands.cinventory(command)
    Jcommands.cshop(command)
    Jcommands.csettings(command)
    # Debug Commands
    Dcommands.cdebug(command)
    Dcommands.caddResources(command)
    return

# Items
def ITEM_LIST(access):
    Jvar.LOADED_RESOURCE_AMOUNT = Jres.shiny_gems
    Jitems.newItem(access,'Shiny Gems','✨💎',40,30)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.cheese_jumpers
    Jitems.newItem(access,'Cheese JumperS','🧀🥋',90,100)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.blue_cheese
    Jitems.newItem(access,'Blue Cheese','Ƀ🧀',90,150)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.pebbles
    Jitems.newItem(access,'Pebbles','⭖',2,5)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.sticks
    Jitems.newItem(access,'Sticks','/',5,10)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.log
    Jitems.newItem(access,'Logs','⍃',15,20)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.ruby
    Jitems.newItem(access,'Rubys','я💎',5,10)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.leaf
    Jitems.newItem(access,'Leaves','🍁',2,5)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.carrot
    Jitems.newItem(access,'Carrots','🥕',15,20)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.potato
    Jitems.newItem(access,'Potatoes','🥔',15,20)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.bread
    Jitems.newItem(access,'Bread','🍞',20,30)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.brick
    Jitems.newItem(access,'Bricks','🧱',10,15)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.mouldyPotato
    Jitems.newItem(access,'Mouldy Potatoes','🕱🥔',10,15)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.child
    Jitems.newItem(access,'Children','🚼',50,60)

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.toyBear
    Jitems.newItem(access,'Toy Bears','🧸',20,30)
    return