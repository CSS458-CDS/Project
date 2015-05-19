"""
class Course
    Members
        term: 0, 1, 2, 3 (Summer, Autum, Winter, Spr)
        requirement: Probably need types for these
        taughtBy: Faculty object
        num: Course number (IE, operating systems is 430)
        timeSlot: Int to indicate what time of day class is taught
        Section: Indicates a different instance of the same class
        Difficulty: from 0 to 1, indicates how difficult a class is (impacts grade distribution)
"""
class Course:
    def __init__(self, quarter=-1, courseNum=None, time=None, day=None, cap=None):
        self.requirement = None
        self.taughtBy = None
        self.section = -1
        self.difficulty = -1
        self.quarter = quarter
        if courseNum is not None:
            self.num = courseNum
        if time is not None:
            self.time = time
        if day is not None:
            self.meetingDays = day
        if cap is not None:
            self.capacity = cap
        else:
            self.num = -1
            self.meetingDays = -1
            self.capacity = -1
            self.time = -1



    def display(self):
        print(self.num, "\t", self.meetingDays, "\t", self.capacity, "\t", self.time)
