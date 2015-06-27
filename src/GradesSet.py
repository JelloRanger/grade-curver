'''
    Filename: GradesSet.py
    Author: Jacob Abramson
    Date created: 6/27/2015
'''

class GradesSet:

    def __init__(self, l):
        self.gradesList = l
        self.origMean = None
        self.curvedMean = None
        self.origStdDev = None
        self.curvedStdDev = None

    def getGradesList(self):
        return self.gradesList

    def setGradesList(self, gl):
        self.gradesList = gl

    def setOrigMean(self, m):
        self.origMean = m

    def setCurvedMean(self, m):
        self.curvedMean = m

    def setOrigStdDev(self, sd):
        self.origStdDev = sd

    def setCurvedStdDev(self, sd):
        self.curvedStdDev = sd

    def getOrigMean(self):
        return self.origMean

    def getCurvedMean(self):
        return self.curvedMean

    def getOrigStdDev(self):
        return self.origStdDev

    def getCurvedStdDev(self):
        return self.curvedStdDev
