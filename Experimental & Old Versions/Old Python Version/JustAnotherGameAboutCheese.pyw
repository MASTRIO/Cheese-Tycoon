## Import Stuff
import PySimpleGUI as sg
import time
# Other Script Resources
import JAGAC_variables
import JAGAC_functions

# Set Theme
sg.theme(JAGAC_variables.GUI_THEME)

# Main Gui Layout
layout1 = [ [sg.Output(size=(50,25), key='-OUTPUT-')],
            [sg.Button('Clear Output')],
            [sg.Text('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')],
            [sg.Text('What do you want to do?')],
            [sg.InputText(do_not_clear=False, tooltip='Type /help for a list of commands'), sg.Button('⭡', tooltip='Run previous command')],
            [sg.Button('Run Command'), sg.Button("Save & Quit")]  ]

# Opens Gui
window1 = sg.Window('Just Another Game About Cheese', layout1)

# Runs when Gui is open
while True:
    event, values = window1.read()
    # Runs when CLOSE is pressed
    if event in (sg.WIN_CLOSED, 'Save & Quit'):
        print('Goodbye :(')
        time.sleep(0.5)
        window1.close()
        break
    if event == 'Clear Output':
        window1['-OUTPUT-'].update('')
    if event == '⭡':
        JAGAC_functions.COMMAND_CHECK(JAGAC_variables.PREVIOUS_COMMAND)
    ## Runs when RUN COMMAND is pressed
    # Checks what command you just ran and executes an action if the correct command is entered
    if event in ('Run Command'):
        JAGAC_functions.COMMAND_CHECK(values[0])
        JAGAC_variables.PREVIOUS_COMMAND = values[0]

# Closes Gui and game
window1.close()