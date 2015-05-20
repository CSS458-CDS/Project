# ===================================================Constant===========================================================
MIN_JUNIOR_CREDIT = 90
AVERAGE_CREDIT_EARNED_PER_YEAR = 45
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
    """
    def __init__(self, courses, senior = False, master = False):
        """
        Description: constructor
        Pre : None
        Post : A student object is appropriately set
        Warning: Do not pass in senior = True and master = True
        Parameters:
            courses: a list of courses that department could offer, in int representation
            senior: a boolean
            master: a boolean
        Returns: None
        """
        self.isSenior = senior
        self.credit = 0
        self.finishedCourses = []
        self.isMaster = master
        self.GPA = N.random.normal(MEAN_GPA,STD)
        if(self.GPA > 4.0):
            self.GPA = 4.0
        elif(self.GPA < 2.0):
            self.GPA = 2.0
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
            # fill in the finishedCourses
            rest = (self.credit - 8 * 5 - MIN_JUNIOR_CREDIT) / 5
            for i in range(0, rest):
                course_index = N.random.randint(0,(courses))
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
            # fill in the finishedCourses
            rest = (self.credit - 8 * 5 - 10 - MIN_JUNIOR_CREDIT) / 5
            for i in range(0, rest):
                course_index = N.random.randint(0,(courses))
                self.finishedCourses.append(courses[course_index])
        # is a junior student
        else:
            # junior student has a range of credit from 90 to 110
            self.credit = MIN_JUNIOR_CREDIT + N.random.randint(0, 5) * 5
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