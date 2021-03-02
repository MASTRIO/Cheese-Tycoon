###########################################
#                                         #
#         The Item API for JAGAC          #
#                                         #
###########################################

# * Import
import variables as Jvar
import resources as Jres

# * API
# Item Manager
def newItem(access,displayName,icon,sellPrice,buyPrice):
    # Sell
    if access == 'sell':
        displayName.lower()
        Jvar.SHOP_COMMAND_STARTING = Jvar.SHOP_COMMAND.startswith('/sell {}'.format(displayName))
        if Jvar.SHOP_COMMAND_STARTING == True:
            Jvar.AMOUNT_TO_SELL = Jvar.CURRENT_SELL_COMMAND.strip('/ abcdefghijklmnopqrstuvwxyz')
            Jvar.AMOUNT_TO_SELL = int(Jvar.AMOUNT_TO_SELL, base=0)

            if Jvar.AMOUNT_TO_SELL > Jvar.LOADED_RESOURCE_AMOUNT:
               print('That number is too high! You only have {} {}'.format(Jvar.LOADED_RESOURCE_AMOUNT,displayName))
            else:
               Jvar.LOADED_RESOURCE_AMOUNT = Jvar.LOADED_RESOURCE_AMOUNT - Jvar.AMOUNT_TO_SELL
               Jres.CHEESE = Jres.CHEESE + (Jvar.AMOUNT_TO_SELL * sellPrice)
               print('You sold', Jvar.AMOUNT_TO_SELL, '🧀🥋', 'for', (Jvar.AMOUNT_TO_SELL * sellPrice))
               print('You now have', Jres.CHEESE, '🧀, and {} 🧀🥋'.format(Jres.CHEESE,Jvar.LOADED_RESOURCE_AMOUNT))
    # Inventory
    if access == 'inventory':
        if Jvar.LOADED_RESOURCE_AMOUNT > 0:
            print('[{}] {} = {}'.format(icon,displayName,Jvar.LOADED_RESOURCE_AMOUNT))
    # Shop
    if access == 'shop':
        if Jvar.LOADED_RESOURCE_AMOUNT > 0:
            print('[{}] {}')
    return