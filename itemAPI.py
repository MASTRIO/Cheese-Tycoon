###########################################
#                                         #
#         The Item API for JAGAC          #
#                                         #
###########################################

# * Import
import technicalVariables as techVar

# * API
# Item Manager
def newItem(displayName,id,icon,amount,sellPrice,buyPrice):
    # Display Name
    if techVar.ITEM_DATA_ACCESS.displayName == True:
        techVar.ITEM_DATA_ACCESS.displayName[False]
        return displayName
    # ID
    if techVar.ITEM_DATA_ACCESS.id == True:
        techVar.ITEM_DATA_ACCESS.id[False]
        return id
    # Icon
    if techVar.ITEM_DATA_ACCESS.icon == True:
        techVar.ITEM_DATA_ACCESS.icon[False]
        return icon
    # Amount
    if techVar.ITEM_DATA_ACCESS.amount == True:
        techVar.ITEM_DATA_ACCESS.amount[False]
        return amount
    # Sell Price
    if techVar.ITEM_DATA_ACCESS.sellPrice == True:
        techVar.ITEM_DATA_ACCESS.sellPrice[False]
        return sellPrice
    # Buy Price
    if techVar.ITEM_DATA_ACCESS.buyPrice == True:
        techVar.ITEM_DATA_ACCESS.buyPrice[False]
        return buyPrice