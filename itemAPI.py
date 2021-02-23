###########################################
#                                         #
#         The Item API for JAGAC          #
#                                         #
###########################################

# * Import
import variables as Jvar

# * API
# Item Manager
def newItem(access,displayName,icon,sellPrice,buyPrice,):
    # Display Name
    if access == 'displayName':
        print(displayName)
        return displayName
    # Icon
    if access == 'icon':
        print(icon)
    # Sell Price
    if access == 'sellPrice':
        return sellPrice
    # Buy Price
    if access == 'buyPrice':
        return buyPrice
    # Inventory
    if access == 'inventory':
        if Jvar.LOADED_RESOURCE_AMOUNT > 0:
            print('[{}] {} = {}'.format(icon,displayName,Jvar.LOADED_RESOURCE_AMOUNT))
    return