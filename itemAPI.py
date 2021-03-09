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
        Jvar.LOWERED_DISPLAY_NAME = displayName.lower()
        Jvar.SHOP_COMMAND_STARTING = Jvar.CURRENT_SHOP_COMMAND.startswith('/sell {}'.format(Jvar.LOWERED_DISPLAY_NAME))
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
    # Convert data to int
    if access == 'convertToInt':
        Jvar.LOADED_RESOURCE_AMOUNT = int(Jvar.LOADED_RESOURCE_AMOUNT)
    # Convert data to str
    if access == 'convertToStr':
        Jvar.LOADED_RESOURCE_AMOUNT = str(Jvar.LOADED_RESOURCE_AMOUNT)
    return