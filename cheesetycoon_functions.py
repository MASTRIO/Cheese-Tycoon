import cheesetycoon_functions
import cheesetycoon_resources

def COMMAND_CHECK(str):
   "UwU"
   if str == '/help':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Here is a list of commands:')
        print('/help\n/balance')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   if str == '/balance':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('You have', cheesetycoon_resources.CHEESE, '🧀 in your wallet')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   if str == '/admin add 10':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('10 🧀 has been added to ya wallet 🍪')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        cheesetycoon_resources.CHEESE = cheesetycoon_resources.CHEESE + 10
   return