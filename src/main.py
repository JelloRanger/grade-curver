'''
    Filename: main.py
    Author: Jacob Abramson
    Date created: 6/26/2015
'''

from GradesSet import GradesSet
from Grade import Grade
#from Window import Window
import math

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

    gradesSet = None

    if isProcessed() is False:
        gradesSet = process()

    # curve based on how far highest grade was from 100
    # (so if highest grade is 82, add 18 points to everyone's grade)
    maxGrade = 0
    for g in gradesSet.getGradesList():
        if g.getOrigGrade() > maxGrade:
            maxGrade = g.getOrigGrade()

    incGrade = 100 - maxGrade
    for g in gradesSet.getGradesList():
        g.setCurvedGrade(g.getOrigGrade() + incGrade)

    # calculate mean/standard deviations
    postCalc(gradesSet)
    
    # write curved grades to txt file
    writeCurvedGrades(gradesSet)

    display(gradesSet)

def postCalc(gradesSet):

    origMean = 0.0
    curvedMean = 0.0
    origStdDev = 0.0
    curvedStdDev = 0.0

    for g in gradesSet.getGradesList():
        # find the mean for orig and curved grades
        origMean += g.getOrigGrade()
        curvedMean += g.getCurvedGrade()

    origMean /= len(gradesSet.getGradesList())
    curvedMean /= len(gradesSet.getGradesList())

    # find the standard deviation for orig and curved grades
    for g in gradesSet.getGradesList():
        origStdDev += (g.getOrigGrade() - origMean)**2
        curvedStdDev += (g.getCurvedGrade() - curvedMean)**2

    origStdDev /= len(gradesSet.getGradesList())
    curvedStdDev /= len(gradesSet.getGradesList())
    origStdDev = math.sqrt(origStdDev)
    curvedStdDev = math.sqrt(curvedStdDev)

    # set the mean/std deviations in the GradesSet object
    gradesSet.setOrigMean(origMean)
    gradesSet.setCurvedMean(curvedMean)
    gradesSet.setOrigStdDev(origStdDev)
    gradesSet.setCurvedStdDev(curvedStdDev)

# process the provided grades txt file
def process():

    origGradesFile = open("grades.txt")
    lines = origGradesFile.readlines()

    gradesList = []

    for line in lines:
        newGrade = Grade(int(line.rstrip()))
        gradesList.append(newGrade)

    origGradesFile.close()

    return GradesSet(gradesList)

# check if grades.txt has been read already
def isProcessed():
    return False

# write the calculated curved grades to a txt file
def writeCurvedGrades(gradesSet):

    # open curved grades txt, create if it doesn't exist
    curvedGradesFile = open("grades_curved.txt", "w")

    for g in gradesSet.getGradesList():
        curvedGradesFile.write(str(g.getCurvedGrade())+"\n")
    

# display original grades (pre curve)
def displayOrigGrades(gradesSet):

    print("Original grades:")
    print("Mean:", gradesSet.getOrigMean())
    print("Std Deviation:", gradesSet.getOrigStdDev())
    for g in gradesSet.getGradesList():
        print(g.getOrigGrade())

# display curved grades
def displayCurvedGrades(gradesSet):

    print("Curved grades:")
    print("Mean:", gradesSet.getCurvedMean())
    print("Std Deviation:", gradesSet.getCurvedStdDev())
    for g in gradesSet.getGradesList():
        print(g.getCurvedGrade())

# display original and curved grades
def display(gradesSet):
    displayOrigGrades(gradesSet)
    displayCurvedGrades(gradesSet)

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
