###########################################
#                                         #
#        The Save System for JAGAC        #
#                                         #
###########################################

# * Imports
import resources as Jres
import functions as Jfunc

# * Code
def loadSaveData():
    # Open save file
    save = open("game.cheeseSave")
    # Get save data
    save.readline() # label
    Jres.CHEESE = save.readline()
    save.readline() # label
    Jres.shiny_gems = save.readline()
    Jres.cheese_jumpers = save.readline()
    Jres.blue_cheese = save.readline()
    Jres.pebbles = save.readline()
    Jres.sticks = save.readline()
    Jres.log = save.readline()
    Jres.ruby = save.readline()
    Jres.leaf = save.readline()
    Jres.carrot = save.readline()
    Jres.potato = save.readline()
    Jres.bread = save.readline()
    Jres.brick = save.readline()
    Jres.mouldy_potato = save.readline()
    Jres.child = save.readline()
    Jres.toy_bear = save.readline()
    # CLose save file
    save.close()

    # Convert data to int
    Jfunc.ITEM_LIST('convertToInt')
    return 

def saveSaveData():
    # Convert data to str
    Jfunc.ITEM_LIST('convertToStr')

    # Open the save file
    save = open("save.cheeseSave", "w")
    # Write data
    save.write("    Currency")
    save.write(Jres.CHEESE)
    save.write("    Resources/Materials")
    save.write(Jres.shiny_gems)
    save.write(Jres.cheese_jumpers)
    save.write(Jres.blue_cheese)
    save.write(Jres.pebbles)
    save.write(Jres.sticks)
    save.write(Jres.log)
    save.write(Jres.ruby)
    save.write(Jres.leaf)
    save.write(Jres.carrot)
    save.write(Jres.potato)
    save.write(Jres.bread)
    save.write(Jres.brick)
    save.write(Jres.mouldy_potato)
    save.write(Jres.child)
    save.write(Jres.toy_bear)
    # Close the save file
    save.close()
    return