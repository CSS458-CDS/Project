"""
class Course
    Members
        term: 0, 1, 2, 3 (Aut, Win, Spr, Sum)
        requirement: Probably need types for these
        taughtBy: Faculty object
        num: Course number (IE, operating systems is 430)
        timeSlot: Int to indicate what time of day class is taught
        Section: Indicates a different instance of the same class
        Difficulty: from 0 to 1, indicates how difficult a class is (impacts grade distribution)
"""
class Course:
    def __init__(self):
        self.term = -1
        self.requirement = None
        self.taughtBy = None
        self.num = -1
        self.timeSlot = -1
        self.section = -1
        self.difficulty = -1