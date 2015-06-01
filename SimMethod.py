import numpy as N
import matplotlib.pyplot as plt
import random as r
from Student import Student
import globals as g
import facultyCourseScheduler
from faculty import faculty
# ===================================================Constant===========================================================
#29.6% Junior
NUM_OF_JUNIOR = int(g.INITIAL_STUDENTS * 0.296)
#55.56% Senior
NUM_OF_SENIOR = int(g.INITIAL_STUDENTS * 0.5556)
#14.8% Master
NUM_OF_MASTER = int(g.INITIAL_STUDENTS * 0.148)
MAX_CLASS_PER_QUARTER = 4
RATE_TO_BE_MASTER = 0.1       # Probability of a graduated student to be a master student
MEAN_GPA = 3.2
STD = 0.5
# ======================================================================================================================

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
    registration(students, courses)
    endOfQuarter(students)
    displayData(students, professors, courses)
    # new junior students come in
    numberOfNew = g.ADMITTED_JUNIORS_PER_QUARTER + (N.random.randint(0,20) - 10)
    for i in range(0, numberOfNew):
        students[0].append(Student(g.ALL_ELECTIVES))
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
    # Shuffle all students
    r.shuffle (students[0])
    r.shuffle (students[1])
    r.shuffle (students[2])
    # register junior
    for i in range(0,len(students[0])):
        # random number of class
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        #shuffle course list
        r.shuffle(courses)
        #register all the possible core classes
        for j in range(0,len(courses)):
            if(courses[j].core == True):
                students[0][i].register(courses[j])
        # if they register more cores than they can register
        if(len(students[0][i].currentCourses) >= numberOfClass):
            students[0][i].currentCourses = students[0][i].currentCourses[:numberOfClass + 1]
        # fill the rest with electives
        else:
            r.shuffle(courses)
            for j in range(0,len(courses)):
                if(courses[j].core == False):
                    students[0][i].register(courses[j])
            # if they register more cores than they can register
            if(len(students[0][i].currentCourses) >= numberOfClass):
                students[0][i].currentCourses = students[0][i].currentCourses[:numberOfClass + 1]
    # register senior
    for i in range(0,len(students[1])):
        # random number of class
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        #register for capstone if they are ready
        if (students[1][i].ready_for_capstone() == True):
            for j in range(0,len(courses)):
                if(courses[j].num == 497):
                    students[1][i].register(courses[j])
        #register all the possible core classes
        #shuffle course list
        r.shuffle(courses)
        for j in range(0,len(courses)):
            if(courses[j].core == True):
                students[1][i].register(courses[j])
        # if they register more cores than they can register
        if(len(students[1][i].currentCourses) >= numberOfClass):
            students[1][i].currentCourses = students[1][i].currentCourses[:numberOfClass + 1]
        # fill the rest with electives
        else:
            # register all the possible elective classes
            #shuffle course list
            r.shuffle(courses)
            for j in range(0,len(courses)):
                if(courses[j].core == False):
                    students[1][i].register(courses[j])
            # if they register more cores than they can register
            if(len(students[1][i].currentCourses) >= numberOfClass):
                students[1][i].currentCourses = students[1][i].currentCourses[:numberOfClass + 1]
    # register master
    for i in range(0,len(students[2])):
        numberOfClass = N.random.randint(1,MAX_CLASS_PER_QUARTER + 1)
        # register 500 level class first
        #shuffle course list
        r.shuffle(courses)
        for j in range(0,len(courses)):
            if(courses[j].num > 500 and courses[j].core != False):
                students[2][i].register(courses[j])
        # if they registered more classes, slice the array
        if(len(students[2][i].currentCourses) >= numberOfClass):
            students[2][i].currentCourses = students[2][i].currentCourses[:numberOfClass + 1]
        else:
            # register 400 level class
            #shuffle course list
            r.shuffle(courses)
            for j in range(0,len(courses)):
                if(courses[j].num > 400 and (courses[j].num < 500 and courses[j].core != False)):
                    students[2][i].register(courses[j])
            # if they registered more classes, slice the array
            if(len(students[2][i].currentCourses) >= numberOfClass):
                students[2][i].currentCourses = students[2][i].currentCourses[:numberOfClass + 1]
    # print end prompt
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
    for i in range(0, 3):
        for j in range(0, len(students[i])):
            # for every class they take
            for k in range(0, len(students[i][j].currentCourses)):
                # course difficulty factor
                difficulty = students[i][j].currentCourses[k].difficulty / ( 2 * 10)
                # receive a GPA for this course
                GPA = N.random.normal(students[i][j].aptitude - difficulty , STD + difficulty)
                # safe boundary
                if(GPA > 4.0):
                    GPA = 4.0
                elif(GPA < 0):
                    GPA = 0
                #update Cumulative GPA
                denominator = (len(students[i][j].finishedCourses) + 90 / 5)
                students[i][j].GPA = (students[i][j].GPA * denominator + GPA) / (denominator + 1)
                # pass the class only when their GPA >= 2.0
                if(GPA >= 2.0):
                    students[i][j].finishedCourses.append(students[i][j].currentCourses[k].num)
                    # students receive 10 credit from capstone
                    if(students[i][j].currentCourses[k].num ==  497):
                        students[i][j].credit += 10
                    else:
                        students[i][j].credit += 5
            # clear their current courses
            students[i][j].currentCourses = []
            # one quarter pasted
            students[i][j].quartersSpent += 1
    # students graduate
    # check all senior students
    i = 0
    graduated = []
    while(i < len(students[1])):
        if (students[1][i].ready_to_graduate() == True):
            #remove student from department
            graduated.append(students[1].pop(i))
            # small chance to become a master student
            if(N.random.rand() < RATE_TO_BE_MASTER):
                students[2].append(graduated[-1])
        else:
            i += 1
    g.student_graduated_quarter.append(graduated)
    g.NUM_GRADUATED += len(graduated)

    # move junior student to senior (spent 4 quarter) if applicable
    i = 0
    while(i < len(students[0])):
            # move to senior
            if(students[0][i].quartersSpent == 4):
                students[1].append(students[0].pop(i))
            else:
                i += 1

# ======================================================================================================================
def displayData(students, professors, courses):
    """
    Description: display the data after this quarter
    Pre : Professors , students and courses have been set
    Post : data and graph are shown
    Parameters: None
    Returns: None
    """
    print('Number of graduated students after this quarter:', len(g.student_graduated_quarter[-1]))
    print('Current junior students:',len(students[0]))
    print('Current senior students:',len(students[1]))
    print('Current master students:',len(students[2]))
    print('Current total students:',(len(students[0])+len(students[1])+len(students[2])))
    g.student_population_quarter.append((len(students[0])+len(students[1])+len(students[2])))
    # students' behavior
    GPA_quarter = []
    for i in range(0, 3):
        for j in range(0, len(students[i])):
            GPA_quarter.append(students[i][j].GPA)
    GPA_quarter = N.array(GPA_quarter)
    print('Current students GPA average:', round(N.mean(GPA_quarter),2))
    g.student_GPA_quarter.append(N.mean(GPA_quarter))
    # number of senior unable to graduate because of not taking capstone
    ungraduated_without_capstone = 0
    for i in range(0, len(students[1])):
        if(497 not in students[1][i].finishedCourses and students[1][i].GPA >= 2.0 and students[1][i].credit >= 180):
            ungraduated_without_capstone += 1
    print('Number of ungraduated Seniors waiting for Capstone:', ungraduated_without_capstone)
    g.ungraduated_without_capstone_quarter.append(ungraduated_without_capstone)
    # number of senior unable to graduate because of not enough credit
    ungraduated_without_credit = 0
    for i in range(0, len(students[1])):
        if(497 in students[1][i].finishedCourses and students[1][i].GPA >= 2.0 and students[1][i].credit < 180):
            ungraduated_without_credit += 1
    print('Number of ungraduated Seniors because of insufficient credit :', ungraduated_without_credit)
    g.ungraduated_without_credit_quarter.append(ungraduated_without_credit)
    # number of senior unable to graduate because of low GPA
    ungraduated_with_low_GPA = 0
    for i in range(0, len(students[1])):
        if(497 in students[1][i].finishedCourses and students[1][i].GPA < 2.0 and students[1][i].credit >= 180):
            ungraduated_with_low_GPA += 1
    print('Number of ungraduated Seniors because of insufficient credit :', ungraduated_with_low_GPA)
    g.ungraduated_with_low_GPA_quarter.append(ungraduated_with_low_GPA)
    # calculate unassigned courses
    unassigned = 0
    for i in range(0, len(courses)):
        if(courses[i].taughtBy == None):
            unassigned+=1
    g.percentage_of_unassigned_courses.append(unassigned / len(courses))
    print('Percentage of Unassigned Courses :', g.percentage_of_unassigned_courses[-1])
# ====================================================main==============================================================
def simulate(years):
    n = years
    # read classes from file
    g.initialize_globals()
    # capstone should not be part of the electives
    g.ALL_ELECTIVES.remove(497)
    # schedule class for whole year
    facultyCourseScheduler.main()
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
    professors = []
    for i in range(n):
        print('-------------------------------Year ', i + 1, '-------------------------------')
        print('Fall:')
        simOneQuarter(students, professors,g.AUTCAT)
        print(' ')
        print('Winter:')
        simOneQuarter(students, professors, g.WINCAT)
        print(' ')
        print('Spring:')
        simOneQuarter(students, professors, g.SPRCAT)
        print(' ')
        print('Summer:')
        simOneQuarter(students, professors, g.SUMCAT)
        print(' ')
        # display graph for the past academic year
        # x coordinate value
        x_value = range(1, ((i + 1) * 4) + 1)
        graduateList = []
        for j in range(len(g.student_graduated_quarter)):
            graduateList.append(len(g.student_graduated_quarter[j]))

        plt.figure(1,figsize=(27, 15), dpi=70,)

        plt.subplot(241)

        plt.plot(x_value,graduateList,'--o')
        # print graduated students
        plt.title('Graduated Students Per Quarter for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],-10, 100])
        plt.xlabel('Quarters')
        plt.ylabel('Number of Graduated Students')
        # print population
        plt.subplot(242)
        plt.plot(x_value,g.student_population_quarter,'--o')
        plt.title(' Students Population for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],0, 400])
        plt.xlabel('Quarters')
        plt.ylabel('Population')

        # display GPA average
        plt.subplot(243)
        plt.plot(x_value,g.student_GPA_quarter,'--o')
        plt.title(' Students GPA Average for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],1, 4])
        plt.xlabel('Quarters')
        plt.ylabel('GPA')

        # display ungraduated data
        plt.subplot(244)
        plt.plot(x_value,g.ungraduated_without_capstone_quarter,'--o')
        plt.title(' Ungraduated Seniors Waiting for Capstone for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],0, 50])
        plt.xlabel('Quarters')
        plt.ylabel('Population')

        plt.subplot(245)
        plt.plot(x_value,g.ungraduated_without_credit_quarter,'--o')
        plt.title(' Ungraduated Seniors with Insufficient Credit for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],0, 150])
        plt.xlabel('Quarters')
        plt.ylabel('Population')

        plt.subplot(246)
        plt.plot(x_value,g.ungraduated_with_low_GPA_quarter,'--o')
        plt.title(' Ungraduated Seniors with Low GPA for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],0, 20])
        plt.xlabel('Quarters')
        plt.ylabel('Population')

        plt.subplot(247)
        plt.plot(x_value,g.percentage_of_unassigned_courses,'--o')
        plt.title(' Percentage of Unassigned Courses for Year: '+ str(i + 1))
        plt.axis([1, x_value[-1],0, 1.0])
        plt.xlabel('Quarters')
        plt.ylabel('Percentage')
        plt.savefig('result_year_'+ str(i+1)+'.png',dpi = 80)
        plt.show()
        #reset course schedule
        AUTCAT = []
        #Course catalog. List of all the courses offered in Winter.
        WINCAT = []
        #Course catalog. List of all the courses offered in Spring.
        SPRCAT = []
        #Course catalog. List of all the courses offered in Summer.
        SUMCAT = []
        allFaculty = []
        ALL_ELECTIVES = []
        # read classes from file
        g.initialize_globals()
        # schedule class for whole year
        facultyCourseScheduler.main()
        # capstone should not be part of the electives
        g.ALL_ELECTIVES.remove(497)

