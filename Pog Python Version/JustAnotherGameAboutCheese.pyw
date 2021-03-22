# * Import Stuff
import PySimpleGUI as sg
import time
# Other Script Resources
import variables as Jvar
import functions as Jfunc
import saveSystem as Jsave
import resources as Jres

# Set Theme
sg.theme(Jvar.GUI_THEME)

# Main Gui Layout
layout1 = [ 
    [sg.Output(size=(50,25), key='-OUTPUT-')],
    [sg.Button('Clear Output')],
    [sg.Text('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')],
    [sg.Text('What do you want to do?')],
    [sg.InputText(do_not_clear=False, tooltip='Type /help for a list of commands'), sg.Button('⭡', tooltip='Run previous command')],
    [sg.Button('Run Command'), sg.Button('Save & Quit')]
]

# Opens Gui
window1 = sg.Window('Just Another Game About Cheese', layout1)

# Loads save data
Jsave.loadSaveData()
Jres.shiny_gems = 10

# Runs when Gui is open
while True:
    event, values = window1.read()
    # Runs when CLOSE is pressed
    if event in (sg.WIN_CLOSED, 'Save & Quit'):
        print('Saving...')
        Jsave.saveSaveData()
        time.sleep(2)
        window1.close()
        break
    if event == 'Clear Output': 
        window1['-OUTPUT-'].update('')
    if event == '⭡':
        Jfunc.COMMAND_LIST(Jvar.PREVIOUS_COMMAND)
    ## Runs when RUN COMMAND is pressed
    # Checks what command you just ran and executes an action if the correct command is entered
    if event in ('Run Command'):
        Jfunc.COMMAND_LIST(values[0])
        Jvar.PREVIOUS_COMMAND = values[0]

# Closes Gui and game
window1.close()