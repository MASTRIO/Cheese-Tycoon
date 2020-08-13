## Import Stuff
import PySimpleGUI as sg
import time
import tkinter as tk
# Other script resources
import cheesetycoon_resources

# Variables
current_command = ''

# Gui Colour
sg.theme('Reddit')
# Main Gui layout
layout = [  [sg.Text('What do you want to do?')],
            [sg.Text('/'),sg.InputText(do_not_clear=False, tooltip='Type /help for command list')],
            [sg.Button('Run Command'), sg.Button('Close')] ]

# Create the Main Gui
window = sg.Window('Cheese Tycoon!', layout)

# Runs events when specific buttons are pressed
while True:
    event, values = window.read()
    # Runs when program is closed
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    ## Runs when the RUN COMMAND button is pressed
    # Create Tkinter Output Window
    root = tk.Tk()
    T = tk.Text(root, height=2, width=30)
    T.pack()
    tk.mainloop()
    # Set Current_command variable to command to run
    current_command = values[0]
    # Checks what command you just ran and executes an action if the correct command is entered
    if current_command == 'test':
        print('testing 1.. 2.. 3..')
    if current_command == 'balance':
        print('You have', cheesetycoon_resources.CHEESE, 'cheese in your wallet')
        T.insert(tk.END, 'You have', cheesetycoon_resources.CHEESE, 'cheese in your wallet')
        
root = tk.Tk()
T = tk.Text(root, height=2, width=30)
T.pack()
T.insert(tk.END, "Just a text Widget\nin two lines\n")
tk.mainloop()

# Close the Window
window.close()