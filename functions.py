###########################################
#                                         #
#       The Function List for JAGAC       #
#                                         #
###########################################

# * Import Stuff
import variables as Jvar
import itemAPI as Jitems
import commandSystem as Jcommands
import resources as Jres
import shop as Scommands

# * Functions
# Commands
def COMMAND_LIST(command):
    command.lower()
    # Normal Commands
    Jcommands.chelp(command)
    Jcommands.cversion(command)
    Jcommands.cbalance(command)
    Jcommands.cinventory(command)
    Jcommands.cshop(command)
    Jcommands.csettings(command)
    # Shop Commands
    Scommands.chelp(command)
    Scommands.csell(command)
    Scommands.cbuy(command)

# Items
def ITEM_LIST(access):
    Jvar.LOADED_RESOURCE_AMOUNT = Jres.shiny_gems
    Jitems.newItem(access,'Shiny Gems','✨💎',40,30)
    Jres.shiny_gems = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.cheese_jumpers
    Jitems.newItem(access,'Cheese JumperS','🧀🥋',90,100)
    Jres.cheese_jumpers = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.blue_cheese
    Jitems.newItem(access,'Blue Cheese','Ƀ🧀',90,150)
    Jres.blue_cheese = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.pebbles
    Jitems.newItem(access,'Pebbles','⭖',2,5)
    Jres.pebbles = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.sticks
    Jitems.newItem(access,'Sticks','/',5,10)
    Jres.sticks = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.log
    Jitems.newItem(access,'Logs','⍃',15,20)
    Jres.log = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.ruby
    Jitems.newItem(access,'Rubys','я💎',5,10)
    Jres.ruby = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.leaf
    Jitems.newItem(access,'Leaves','🍁',2,5)
    Jres.leaf = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.carrot
    Jitems.newItem(access,'Carrots','🥕',15,20)
    Jres.carrot = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.potato
    Jitems.newItem(access,'Potatoes','🥔',15,20)
    Jres.potato = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.bread
    Jitems.newItem(access,'Bread','🍞',20,30)
    Jres.bread = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.brick
    Jitems.newItem(access,'Bricks','🧱',10,15)
    Jres.brick = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.mouldy_potato
    Jitems.newItem(access,'Mouldy Potatoes','🕱🥔',10,15)
    Jres.mouldy_potato = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.child
    Jitems.newItem(access,'Children','🚼',50,60)
    Jres.child = Jvar.LOADED_RESOURCE_AMOUNT

    Jvar.LOADED_RESOURCE_AMOUNT = Jres.toy_bear
    Jitems.newItem(access,'Toy Bears','🧸',20,30)
    Jres.toy_bear = Jvar.LOADED_RESOURCE_AMOUNT
    return