"""This is a test file that tests the student class"""
import numpy as N
from Student import Student
import globals as g
g.get_all_electives()

# initialize students
junior=[]
for i in range(0,40):
    junior.append(Student(g.ALL_ELECTIVES))
senior=[]
for i in range(0,40):
    senior.append(Student(g.ALL_ELECTIVES,True))
master=[]
for i in range(0,40):
    master.append(Student(g.ALL_ELECTIVES,False,True))

def simOneQuarter():
    """
    Description: run simulation for one quarter
    Pre : 1. Professors and courses have been set
    Post : A student object is appropriately set
    Warning: Do not pass in senior = True and master = True
    Parameters:
        courses: a list of courses that department could offer, in int representation
        senior: a boolean
        master: a boolean
    Returns: None
    """