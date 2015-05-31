# ===================================================Constant===========================================================
MIN_JUNIOR_CREDIT = 90
AVERAGE_CREDIT_EARNED_PER_YEAR = 40
MIN_SENIOR_CREDIT = MIN_JUNIOR_CREDIT + AVERAGE_CREDIT_EARNED_PER_YEAR
MEAN_GPA = 3.2
STD = 0.5
MIN_GPA_TO_GRADUATE = 2.0
# ======================================================================================================================

import numpy as N
class Student(object):
    """
    class Student
        Attribute:
            isSenior: a boolean that determines whether a student to be initialized is a junior or senior
            isMaster: a boolean that determines whether a student to be initialized is a master
            credit: an int representing the total credit a student has earned
            finishedCourses: a list that contains all the course number
            GPA: a double that represent the cumulative GPA
            currentCourses: a list of course class that the student is taking this quarter
    """
    # ==================================================================================================================
    def __init__(self, courses, senior = False, master = False):
        """
        Description: constructor
        Pre : None
        Post : A student object is appropriately set
        Warning: Do not pass in senior = True and master = True
        Parameters:
            courses: a list of elective courses that department could offer, in int representation
            senior: a boolean
            master: a boolean
        Returns: None
        """
        self.isSenior = senior
        self.credit = 0
        self.finishedCourses = []
        self.currentCourses = []
        self.isMaster = master
        self.quartersSpent = 0
        self.GPA = N.random.normal(MEAN_GPA,STD)
        if(self.GPA > 4.0):
            self.GPA = 4.0
        elif(self.GPA < 2.0):
            self.GPA = 2.0

        #Use as mean for random GPA generation
        self.aptitude = self.GPA
        # is a senior student
        if(self.isSenior == True):
            # initialize credit
            self.credit = MIN_SENIOR_CREDIT + N.random.randint(0, 5) * 5
            # assign core classes
            self.finishedCourses.append(342)
            self.finishedCourses.append(343)
            self.finishedCourses.append(301)
            self.finishedCourses.append(350)
            self.finishedCourses.append(360)
            self.finishedCourses.append(370)
            self.finishedCourses.append(422)
            self.finishedCourses.append(430)
            self.finishedCore = self.finishedCourses
            self.quartersSpent = 4
            # fill in the finishedCourses
            rest = int((self.credit - 8 * 5 - MIN_JUNIOR_CREDIT) / 5)

            for i in range(0, rest):
                course_index = N.random.randint(0,len(courses))
                self.finishedCourses.append(courses[course_index])
        # is a master student
        elif(self.isMaster == True):
            self.credit = 180
            # assign core classes
            self.finishedCourses.append(342)
            self.finishedCourses.append(343)
            self.finishedCourses.append(301)
            self.finishedCourses.append(350)
            self.finishedCourses.append(360)
            self.finishedCourses.append(370)
            self.finishedCourses.append(422)
            self.finishedCourses.append(430)
            self.finishedCourses.append(497)
            self.finishedCore = self.finishedCourses
            self.quartersSpent = 8
            # fill in the finishedCourses
            rest = int((self.credit - 8 * 5 - 10 - MIN_JUNIOR_CREDIT) / 5)
            for i in range(0, rest):
                course_index = N.random.randint(0,len(courses))
                self.finishedCourses.append(courses[course_index])
        # is a junior student
        else:
            # junior student has a range of credit from 90 to 110
            self.credit = MIN_JUNIOR_CREDIT + N.random.randint(0, 5) * 5
    # ==================================================================================================================
    def ready_to_graduate(self):
        """
        Description: tell whether a student is good to graduate
        Pre : student properties are appropriately set
        Post : A boolean is returned
        Parameters: None
        Returns: True if student finishes capstone and have more than 180 credits and more than MIN_GPA_TO_GRADUATE
                 False otherwise
        """
        if( 497 in self.finishedCourses and self.credit >= 180 and self.GPA >= MIN_GPA_TO_GRADUATE):
            return True
        else:
            return False
    # ==================================================================================================================
    def ready_for_capstone(self):
        """
        Description: tell whether a student is able to register capstone
        Pre : student properties are appropriately set
        Post : A boolean is returned
        Parameters: None
        Returns: True if student finishes all core classes
                 False otherwise
        """
        if( 301 in self.finishedCourses and
            342 in self.finishedCourses and
            343 in self.finishedCourses and
            350 in self.finishedCourses and
            360 in self.finishedCourses and
            370 in self.finishedCourses and
            422 in self.finishedCourses and
            430 in self.finishedCourses):
            return True
        else:
            return False
    # ==================================================================================================================
    def have_taken(self, course):
        """
        Description: tell whether a student has taken a certain course
        Pre : student properties are appropriately set
        Post : A boolean is returned
        Parameters:
                    course: int
        Returns: True if student has taken the course
                 False otherwise
        """
        if(course in self.finishedCourses):
            return True
        else:
            return False
    # ==================================================================================================================
    def register(self, course):
        """
        Description: add a course object to currentCourses,
        Pre : student properties are appropriately set
        Post : A course object have been added, bool is returned
        Parameters:
            course: course object
        Returns: True if registration is successful, false otherwise
        """
        # this student is able to register for a certain course if
        # 1.course is not full
        # 2.no time conflict
        # 3.No retaking
        # todo: 4.course cant be taughtBy = None
        if ( course.spots > 0 and self.timeConflict(course) == False and course.num not in self.finishedCourses):
            # student tries to register capstone
            if(self.ready_for_capstone() and course.num == 497):
                course.spots -= 1
                self.currentCourses.append(course);
                return True
            elif(course.num != 497):
                course.spots -=1
                self.currentCourses.append(course);
                return True
            else:
                return False
        else:
            return False
    # ==================================================================================================================
    def timeConflict(self,course):
        """
        Description: determines whether the course to be registered has time conflicts with registered classes
        Pre : student properties are appropriately set
        Post : boolean is returned
        Parameters:
            course: course object
        Returns: True if time conflicts, false otherwise
        """
        # haven't registered for any courses
        if(len(self.currentCourses) == 0):
            return False
        else:
            for i in range(0,len(self.currentCourses) ):
                # compare with the time
                if(self.currentCourses[i].time == course.time and self.dayConflict(self.currentCourses[i].meetingDays,course.meetingDays) == True):
                    return True
            return False

    # ==================================================================================================================
    def dayConflict(self, daylist1, daylist2):
        """
        Description: determines whether two day list conficts
        Pre : two lists are set
        Post : boolean is returned
        Parameters:
            course: course object
        Returns: True if day conflicts, false otherwise
        """
        for i in range(0, len(daylist2)):
            if(daylist2[i] in daylist1):
                return True
        return False