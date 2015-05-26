# ===================================================Constant===========================================================
NUM_OF_JUNIOR = 80
NUM_OF_SENIOR = 150
NUM_OF_MASTER = 40
MAX_CLASS_PER_QUARTER = 4
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
    # register junior
    for i in range(0,len(students[0])):
        # random number of class
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        #register all the possible core classes
        for j in range(0,len(courses)):
            if(courses[j].core == True):
                students[i].register(courses[j])
        # if they register more cores than they can register
        if(len(students[i].currentCourses) >= numberOfClass):
            students[i].currentCourses = students[i].currentCourses[:numberOfClass + 1]
        # fill the rest with electives
        else:
            for j in range (0, (numberOfClass - len(students[i].currentCourses))):
                keepLooping = True
                while(keepLooping):
                    index = N.random.randin(0,len(courses))
                    if(courses[index].elective == True and students[i].register(courses[index]) == True):
                        keepLooping = False
                    else
                        keepLooping = True
    # register senior



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
# ======================================================================================================================
def moveToJunior(junior,senior):
    """
    Description: move junior to senior when the quarter they spend is 4
    Pre : junior students has been set
    Post :junior students has been moved
    Parameters: junior: a list of junior students
                senior: a list of senior students
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
