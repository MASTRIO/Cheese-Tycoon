## Import Stuff
import PySimpleGUI as sg
import time
import keyboard
# Other Script Resources
import JAGAC_variables
import JAGAC_functions

# Set Theme
sg.theme(JAGAC_variables.GUI_THEME)

# Main Gui Layout
layout = [  [sg.Output(size=(50,25), key='-OUTPUT-')],
            [sg.Button('Clear Output')],
            [sg.Text('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')],
            [sg.Text('What do you want to do?')],
            [sg.InputText(do_not_clear=False, tooltip='Type /help for command list')],
            [sg.Button('Run Command'), sg.Button('Close')]  ]

# Opens Gui
window = sg.Window('Just Another Game About Cheese - v0.1', layout)

# Runs when Gui is open
while True:
    event, values = window.read()
    # Runs when CLOSE is pressed
    if event in (sg.WIN_CLOSED, 'Close'):
        print('Goodbye :(')
        time.sleep(0.5)
        break
    if event == 'Clear Output':
        window['-OUTPUT-'].update('')
    ## Runs when RUN COMMAND is pressed
    # Checks what command you just ran and executes an action if the correct command is entered
    if event in ('Run Command'):
        JAGAC_functions.COMMAND_CHECK(values[0])

# Closes Gui and game
window.close()