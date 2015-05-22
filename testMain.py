# ===================================================Constant===========================================================
NUM_OF_JUNIOR = 80
NUM_OF_SENIOR = 150
NUM_OF_MASTER = 40
# ======================================================================================================================
import numpy as N
from Student import Student
import globals as g

# ======================================================================================================================
def simOneQuarter(students, professors, courses):
    """
    Description: run simulation for one quarter
    Pre : Professors , students and courses have been set
    Post : One simulation is finished
    Parameters:
                students: a 2D list of students
                    students[0] is junior
                    students[1] is senior
                    students[2] is master
                professors: a list of faculty objects
                courses: a list of course objects
    Returns: None
    """
    scheduleClass(courses, professors)
    registration(students, courses)
    endOfQuarter(students)
# ======================================================================================================================
def scheduleClass(course, professors):
    """
    Description: assign professors with classes
    Pre : Professors and courses have been read
    Post : professor and courses are set
    Parameters:
                professors: a list of faculty objects
                courses: a list of course objects
    Returns: None
    """
# ======================================================================================================================
def registration(students, courses):
    """
    Description: junior, senior and master students register for class
    Pre : Professors , students and courses have been set
    Post : classes are fulfilled
    Parameters:
                students: a 2D list of students
                    students[0] is junior
                    students[1] is senior
                    students[2] is master
                courses: a list of course objects
    Returns: None
    """
# ======================================================================================================================
def endOfQuarter(students):
    """
    Description: students are graded for their course and new junior students are coming in and graduated students are
                 removed/get placed to master
    Pre : Professors , students and courses have been set
    Post : grades are updated, new juniors are initialized, graduated students are removed
    Parameters:
                students: a 2D list of students
                    students[0] is junior
                    students[1] is senior
                    students[2] is master
    Returns: None
    """
    displayData()
# ======================================================================================================================
def displayData():
    """
    Description: display the data after this quarter
    Pre : Professors , students and courses have been set
    Post : data and graph are shown
    Parameters: None
    Returns: None
    """

# ====================================================main==============================================================

# read classes from file
g.initialize_globals()
#initialize students
junior=[]
for i in range(0,NUM_OF_JUNIOR):
    junior.append(Student(g.ALL_ELECTIVES))
senior=[]
for i in range(0,NUM_OF_SENIOR):
    senior.append(Student(g.ALL_ELECTIVES,True))
master=[]
for i in range(0,NUM_OF_MASTER):
    master.append(Student(g.ALL_ELECTIVES,False,True))
students  = [junior, senior, master]
# 0 - 3 corresponds to fall, winter, spring summer
courses = [g.AUTCAT,g.WINCAT,g.SPRCAT,g.SUMCAT]
# initialize professors
professors = []
# run model for 1 year
for i in range(0,4):
    simOneQuarter(students, professors, courses[i])
