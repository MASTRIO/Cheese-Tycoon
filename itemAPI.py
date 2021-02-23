###########################################
#                                         #
#         The Item API for JAGAC          #
#                                         #
###########################################

# * Import
import variables as Jvar

# * API
# Item Manager
def newItem(displayName,icon,sellPrice,buyPrice,):
    # Display Name
    if Jvar.ITEM_DATA_ACCESS.displayName == True:
        Jvar.ITEM_DATA_ACCESS.displayName[False]
        print(displayName)
        return displayName
    # Icon
    if Jvar.ITEM_DATA_ACCESS.icon == True:
        Jvar.ITEM_DATA_ACCESS.icon[False]
        print(icon)
    # Sell Price
    if Jvar.ITEM_DATA_ACCESS.sellPrice == True:
        Jvar.ITEM_DATA_ACCESS.sellPrice[False]
        return sellPrice
    # Buy Price
    if Jvar.ITEM_DATA_ACCESS.buyPrice == True:
        Jvar.ITEM_DATA_ACCESS.buyPrice[False]
        return buyPrice
    # Inventory
    if Jvar.ITEM_DATA_ACCESS.inventory == True:
        Jvar.ITEM_DATA_ACCESS.inventory[False]
        print("[" + icon + "] " + displayName + " =" + Jvar.LOADED_RESOURCE_AMOUNT)
    return