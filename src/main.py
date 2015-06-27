'''
    Filename: main.py
    Author: Jacob Abramson
    Date created: 6/26/2015
'''

# introduce the user
def start():
    print("~~~~~~~~~~~ Welcome to Grade Curver! ~~~~~~~~~~~~")
    print("=================================================")
    print("If this is your first time using Grade Curver")
    print("then please refer to the README for instructions.")
    print("Type help for additional commands")
    print("=================================================")
    loop()

# help method
def _help():
    print("Commands:")

# main loop to interface with the user
def loop():

    while True:

        # read in command
        command = input("> ")

        if command == "help":
            _help()
            

# begin execution of the application
start()
