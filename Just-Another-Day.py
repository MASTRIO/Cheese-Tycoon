## Import Stuff
import PySimpleGUI as sg
import time
# Other Script Resources
import JustAnotherDay_variables
import JustAnotherDay_functions

# Set Theme
sg.theme('NeutralBlue')
# Gui Layout
layout = [  [sg.Output(size=(50,25), key='-OUTPUT-')],
            [sg.Button('Clear Output')],
            [sg.Text('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')],
            [sg.Text('What do you want to do?')],
            [sg.InputText(do_not_clear=False, tooltip='Type /help for command list')],
            [sg.Button('Run Command'), sg.Button('Close')]  ]

# Opens Gui
window = sg.Window('Just Another Day v0.1', layout)

# Runs when Gui is open
while True:
    event, values = window.read()
    # Runs when CLOSE is pressed
    if event in (sg.WIN_CLOSED, 'Close'):
        break
    if event == 'Clear Output':
        window['-OUTPUT-'].update('')
    ## Runs when RUN COMMAND is pressed
    # Set Current_command variable to command to run
    current_command = values[0]
    # Checks what command you just ran and executes an action if the correct command is entered
    JustAnotherDay_functions.COMMAND_CHECK(values[0])

# Close Gui
window.close()