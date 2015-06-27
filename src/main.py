'''
    Filename: main.py
    Author: Jacob Abramson
    Date created: 6/26/2015
'''

from Grade import Grade

# list of grade objects
gradesList = []

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
    print("~~~~~~~~~~~~~~~~~~~~~~~~~ Help ~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("To begin, please enter in a list of grades in grades.txt")
    print("Format:")
    print("96\n72\n85\n...")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# calculate curve
def calc():

    if isProcessed() is False:
        process()

    # curve based on how far highest grade was from 100
    # (so if highest grade is 82, add 18 points to everyone's grade)
    maxGrade = 0
    for g in gradesList:
        if g.getOrigGrade() > maxGrade:
            maxGrade = g.getOrigGrade()

    incGrade = 100 - maxGrade
    for g in gradesList:
        g.setCurvedGrade(g.getOrigGrade() + incGrade)

    display()

def process():

    origGradesFile = open("grades.txt")
    lines = origGradesFile.readlines()

    for line in lines:
        newGrade = Grade(int(line.rstrip()))
        gradesList.append(newGrade)

    origGradesFile.close()

def isProcessed():
    return False

def displayOrigGrades():

    print("Original grades:")
    for g in gradesList:
        print(g.getOrigGrade())

def displayCurvedGrades():

    print("Curved grades:")
    for g in gradesList:
        print(g.getCurvedGrade())

def display():
    displayOrigGrades()
    displayCurvedGrades()

# main loop to interface with the user
def loop():

    while True:

        # read in command
        command = input("> ")

        if command == "help":
            _help()
        elif command == "calc":
            calc()
        elif command == "display":
            display()

# begin execution of the application
start()
