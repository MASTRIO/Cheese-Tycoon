# Import stuff
import PySimpleGUI as sg
import JAGAC_variables

# Sell Menu Layout
Layout = [[sg.Output(size=(30,30))]
         [sg.Text('Hello')]
         ]

sg.theme(JAGAC_variables.GUI_THEME)
# The function to open the window
def OPEN_SELL_WINDOW():
    window = sg.Window('JAGAC - Sell Menu', layout)