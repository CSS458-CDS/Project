import course as c
import globals as g
"""---------------------------------------
Creates course objects from a text file fileName

File format: The second line is quarters (i.e., Summer Au Win Spr)
Course data starts on the 4th line
A line looks like
[Course number] [startTime-endTime] [day/day] [capacity]

"""
def buildClasses(fileName=g.COURSE_SOURCE_FILE):
    f = open(fileName, 'r+')
    #Ignore heading lines
    for i in range(3):
        f.readline()
    for lines in f:
        tokens = f.readline().split()
        print(tokens)
        g.SUMCAT.append(c.Course(0, tokens[0:4]))
        g.AUTCAT.append(c.Course(1, tokens[4:8]))
        g.WINCAT.append(c.Course(2, tokens[8:12]))
        g.SPRCAT.append(c.Course(3, tokens[12:16]))





buildClasses()