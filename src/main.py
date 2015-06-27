'''
    Filename: main.py
    Author: Jacob Abramson
    Date created: 6/26/2015
'''

from Grade import Grade
from Window import Window

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

    writeCurvedGrades()

    display()

# process the provided grades txt file
def process():

    origGradesFile = open("grades.txt")
    lines = origGradesFile.readlines()

    for line in lines:
        newGrade = Grade(int(line.rstrip()))
        gradesList.append(newGrade)

    origGradesFile.close()

# check if grades.txt has been read already
def isProcessed():
    return False

# write the calculated curved grades to a txt file
def writeCurvedGrades():

    # open curved grades txt, create if it doesn't exist
    curvedGradesFile = open("grades_curved.txt", "w")

    for g in gradesList:
        curvedGradesFile.write(str(g.getCurvedGrade())+"\n")
    

# display original grades (pre curve)
def displayOrigGrades():

    print("Original grades:")
    for g in gradesList:
        print(g.getOrigGrade())

# display curved grades
def displayCurvedGrades():

    print("Curved grades:")
    for g in gradesList:
        print(g.getCurvedGrade())

# display original and curved grades
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
        elif command == "exit":
            break

# begin execution of the application
start()
