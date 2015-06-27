'''
    Filename: Grade.py
    Author: Jacob Abramson
    Date created: 6/26/2015
'''

class Grade:

    def __init__(self, g):
        self.origGrade = g

    def setCurvedGrade(self, g):
        self.curvedGrade = g

    def getOrigGrade(self):
        return self.origGrade

    def getCurvedGrade(self):
        return self.curvedGrade
