# ===================================================Constant===========================================================
NUM_OF_JUNIOR = 80
NUM_OF_SENIOR = 150
NUM_OF_MASTER = 40
MAX_CLASS_PER_QUARTER = 4
RATE_TO_BE_MASTER = 0.1       # Probability of a graduated student to be a master student
# ======================================================================================================================
import numpy as N
from Student import Student
import globals as g
from faculty import faculty

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
    #scheduleClass(courses, professors)
    registration(students, courses)
    endOfQuarter(students)
    displayData(students, professors, courses)
    # new junior students come in
    numberOfNew = NUM_OF_JUNIOR/2 +  N.random.randint(0,NUM_OF_JUNIOR/2)
    for i in range(0, numberOfNew):
        students[0].append(Student(g.ALL_ELECTIVES))
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
    # print out prompt line
    print('Registration Period Starts:')
    for i in range(0,len(students[0])):
        # random number of class
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        #register all the possible core classes
        for j in range(0,len(courses)):
            if(courses[j].core == True):
                students[0][i].register(courses[j])
        # if they register more cores than they can register
        if(len(students[0][i].currentCourses) >= numberOfClass):
            students[0][i].currentCourses = students[0][i].currentCourses[:numberOfClass + 1]
        # fill the rest with electives
        else:
            for j in range (0, (numberOfClass - len(students[0][i].currentCourses))):
                keepLooping = True
                while(keepLooping):
                    index = N.random.randin(0,len(courses))
                    if(courses[index].elective == True and students[0][i].register(courses[index]) == True):
                        keepLooping = False
                    else:
                        keepLooping = True
    # register senior
    for i in range(0,len(students[1])):
        # random number of class
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        #register for capstone
        #if they are ready
        if (students[1][i].ready_for_capstone() == True):
            for j in range(0,len(courses)):
                if(courses[j].num == 497):
                    students[1][i].register(courses[j])
        #register all the possible core classes
        for j in range(0,len(courses)):
            if(courses[j].core == True):
                students[1][i].register(courses[j])
        # if they register more cores than they can register
        if(len(students[1][i].currentCourses) >= numberOfClass):
            students[1][i].currentCourses = students[1][i].currentCourses[:numberOfClass + 1]
        # fill the rest with electives
        else:
            for j in range (0, (numberOfClass - len(students[1][i].currentCourses))):
                keepLooping = True
                while(keepLooping):
                    index = N.random.randin(0,len(courses))
                    if(courses[index].elective == True and students[1][i].register(courses[index]) == True):
                        keepLooping = False
                    else:
                        keepLooping = True
    # register master
    for i in range(0,len(students[2])):
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        # register 500 level class first
        for j in range(0,len(courses)):
            if(courses[j].num > 500):
                students[2][i].register(courses[j])
        # if they registered more classes, slice the array
        if(len(students[2][i].currentCourses) >= numberOfClass):
            students[2][i].currentCourses = students[2][i].currentCourses[:numberOfClass + 1]
        else:
            # register 400 level class
            for j in range(0,len(courses)):
                if(courses[j].num > 400 and (courses[j].num < 500)):
                    students[2][i].register(courses[j])
            # if they registered more classes, slice the array
            if(len(students[2][i].currentCourses) >= numberOfClass):
                students[2][i].currentCourses = students[2][i].currentCourses[:numberOfClass + 1]
    # print end prompt
    print('Registration Period Ends:')
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
    # students gets their grade
    print('Grading Period Starts')
    for i in range(0, 3):
        for j in range(0, len(students[i])):
            # for every class they take
            for k in range(0, len(students[i][j]).currentCourses):
                # receive a GPA for this course
                GPA =  N.random.normal(Student.MEAN_GPA,Student.STD)
                if(GPA > 4.0):
                    GPA = 4.0
                elif(GPA < 2.0):
                    GPA = 2.0
                #update Cumulative GPA
                denominator = (len(students[i][j].finishedCourses) + 90 / 5)
                students[i][j].GPA = (students[i][j].GPA * denominator + GPA) / (denominator + 1)
                # pass the class only when their GPA >= 2.0
                if(GPA >= 2.0):
                    students[i][j].finishedCourses.append(students[i][j].currentCourses[k].num)
            # clear their current courses
            students[i][j].currentCourses = []
            # one quarter pasted
            students[i][j].quartersSpent += 1
    print('Grading Period Ends')
    # students graduate
    # check all senior students
    for i in range(0, len(students[1])):
        if (students[1][i].ready_to_graduate() == True):
            #remove student from department
            g.graduated_students.append(students[1].pop(i))
            # small chance to become a master student
            if(N.random.rand() < RATE_TO_BE_MASTER):
                students[2].append(g.graduated_students[-1])
    # move junior student to senior (spent 4 quarter) if applicable
    for i in range(0, len(students[0])):
        if(students[0][i].quartersSpent == 4):
            # move to senior
            students[1].append(students[0].pop(i))
# ======================================================================================================================
def displayData(students, professors, courses):
    """
    Description: display the data after this quarter
    Pre : Professors , students and courses have been set
    Post : data and graph are shown
    Parameters: None
    Returns: None
    """
    print('Number of graduated students after this quarter:', len(g.graduated_students))
    print('Current junior students:',len(students[0]))
    print('Current senior students:',len(students[1]))
    print('Current master students:',len(students[2]))
    print('Current total students:',(len(students[0])+len(students[1])+len(students[2])))



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
print(len(g.allFaculty))
for i in range(0, len(g.allFaculty)):
    print(g.allFaculty[i],lastName)
# run model for 1 year
# for i in range(0,4):
#     simOneQuarter(students, professors, courses[i])
