
import globals as g
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
        dept: The department that the class is in. i.e., CSS, BCUSP
        field: The desired expertise
"""
#Sections happen when multiple courses with the same number are added
#The parenthesis in the course title refer to foot notes, and can be ignored
#The one with the comma
#TODO Make it so -1 values arent returned in make_one_class
#TODO What's up with css515
#TODO Title lookup for non-CSS
class Course:
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
            spots: 0 to capacity, the spots left in this course
    """
    def __init__(self, quarter=-1, courseNum=None, time=None, day=None, cap=None):
        self.requirement = None
        self.taughtBy = None
        self.field = "Default Field"
        self.section = -1
        self.dept = []
        self.title = "Default Title"
        self.difficulty = -1
        self.quarter = quarter
        self.core = False
        self.elective = False
        self.lab = False
        if courseNum is not None:
            self.num = courseNum
        if time is not None:
            self.time = time
        if day is not None:
            self.meetingDays = day
        if cap is not None:
            self.capacity = cap
            self.spots = cap
        else:
            self.num = -1
            self.meetingDays = -1
            self.capacity = -1
            self.time = -1


    def display(self, title=False):
        if self.section != -1 and title:
            print(self.dept, self.num, self.title, self.section, "\t", self.meetingDays, "\t", self.capacity, "\t", self.time)
        if self.section != -1 and not title:
            print(self.dept, self.num, self.section, "\t", self.meetingDays, "\t", self.capacity, "\t", self.time)

        else:
            if title:
                print(self.dept, self.num, self.title, "\t", self.meetingDays, "\t", self.capacity, "\t", self.time)
            else:
                print(self.dept, self.num, "\t", self.meetingDays, "\t", self.capacity, "\t", self.time)


    """
    Use the course num to navigate a series of if statements to find the string title of the course.
    Pre: Course has no title
    Post: Course now has a title

    515: Doesnt seem to be offered
    205/405: Women in stem
    """
    def getCourseData(self):
        self.num = int(self.num)
        if self.num in g.CORE_CLASSES:
            self.core = True
        else:
            self.elective = True
    def getTitle(self):
        self.num = int(self.num)
        if self.dept == "CSS":
            if self.num == 107:
                self.title = "Introduction to Programming through Animated Storytelling"
                self.set_field(0)
            elif self.num == 161:
                self.title = "Fundamentals Of Computing"
                self.set_field(0)

            elif self.num == 162:
                self.title = "Programming Methodology"
                self.set_field(0)
            elif self.num == 211:
                self.title = "Computers and Society"
                self.set_field(12)
            elif self.num == 225:
                self.title = "Physics and Chemistry of Computer Components and Their Manufacture"
                self.set_field(10)
            elif self.num == 290:
                self.title = "Topics in Computing"
                self.set_field(12)
            elif self.num == 295:
                self.title = "K-12 Computing Education"
                self.set_field(9)
            elif self.num == 301:
                self.title = "Technical Writing"
                self.set_field(6)
            elif self.num == 310:
                self.title = "Information Assurance and Cyber Security"
                self.set_field(5)
            elif self.num == 332:
                self.title = "Programming Issues with Object-Oriented Languages"
                self.set_field(0)
            elif self.num == 337:
                self.title = "Secure Systems"
                self.set_field(5)
            elif self.num == 341:
                self.title = "Fundamentals of Programming Theory and Applications"
                self.set_field(0)
            elif self.num == 342:
                self.title = "Data Structures, Algorithms, and Discrete Mathematics I"
                self.set_field(0)
            elif self.num == 343:
                self.title = "Data Structures, Algorithms, and Discrete Mathematics II"
                self.set_field(0)
            elif self.num == 350:
                self.title = "Management Principles for Computing Professionals"
                self.set_field(9)
            elif self.num == 360:
                self.title = "Software Engineering"
                self.set_field(2)
            elif self.num == 370:
                self.title = "Analysis and Design"
                self.set_field(2)
            elif self.num == 371:
                self.title = "The Business of Technology"
                self.set_field(12)
            elif self.num == 383:
                self.title = "Bioinformatics"
                self.set_field(1)
            elif self.num == 385:
                self.title = "Introduction to Game Development"
                self.set_field(11)
            elif self.num == 405:
                self.title = "Women in STEM Seminar: Career/Professional Life"
                self.set_field(12)
            elif self.num == 411:
                self.title = "Computing Technology and Public Policy"
                self.set_field(12)
            elif self.num == 415:
                self.title = "Emerging Topics in Information Assurance and Cybersecurity"
                self.set_field(5)
            #TODO
            elif self.num == 421:
                self.title = "Introduction to Hardware and Operating Systems"
                self.set_field(4)
                self.set_field(3)
            elif self.num == 422:
                self.title = "Hardware and Computer Organization"
                self.set_field(4)
            elif self.num == 427:
                self.title = "Introduction to Embedded Systems"
                self.set_field(4)
            elif self.num == 428:
                self.title = "Advanced Embedded Systems"
                self.set_field(4)
            elif self.num == 430:
                self.title = "Operating Systems"
                self.set_field(3)
            elif self.num == 432:
                self.title = "Network Design"
                self.set_field(8)
            elif self.num == 434:
                self.title = "Parallel and Distributed Computing"
                self.set_field(8)
            elif self.num == 448:
                self.title = "Introduction to Compilers"
                self.set_field(0)
            elif self.num == 451:
                self.title = "3-D Computer Graphics"
                self.set_field(11)
            elif self.num == 455:
                self.title = "Introduction to Computational Science and Scientific Programming"
                self.set_field(1)
            #TODO
            elif self.num == 457:
                self.title = "Multimedia and Signal Computing"
                self.set_field(4)
            elif self.num == 458:
                self.title = "Fundamentals of Computer Simulation Theory and Application"
                self.set_field(1)
            elif self.num == 473:
                self.title = "Entrepreneurship Seminar"
            elif self.num == 474:
                self.title = "Product Development Lab"
            elif self.num == 475:
                self.title = "Database Systems"
                self.set_field(7)
            elif self.num == 480:
                self.title = "480 Principles of Human-Computer Interaction"
            elif self.num == 490:
                self.title = "Special Topics in Computing and Software Systems"
            elif self.num == 495:
                self.title = "Applied Computing Internship"
            elif self.num == 496:
                self.title = "Applied Computing Capstone"
            elif self.num == 497:
                self.title = "Computer Science and Software Engineering Capstone"
            elif self.num == 498:
                self.title = "Independent Study"
            elif self.num == 499:
                self.title = "Undergraduate Research"
            elif self.num == 501:
                self.title = "Data Structures and Object-Oriented Programming I"
                self.set_field(0)
            elif self.num == 502:
                self.title = "Data Structures and Object-Oriented Programming II"
                self.set_field(0)
            elif self.num == 503:
                self.title = "Systems Programming"
                self.set_field(0)
            elif self.num == 506:
                self.title = "Software Development Processes"
                self.set_field(2)
            elif self.num == 507:
                self.title = "Software Modeling Techniques"
                self.set_field(2)
            elif self.num == 508:
                self.title = "Software Testing and Quality"
                self.set_field(0)
            elif self.num == 514:
                self.title = "Security, Policy, Ethics, and the Legal Environment"
                self.set_field(5)
            elif self.num == 517:
                self.title = "Information Assurance and the Secure Development Lifecycle"
                self.set_field(2)
                self.set_field(5)
            elif self.num == 519:
                self.title = "Incident Response and Recovery"
                self.set_field(5)
            elif self.num == 527:
                self.title = "Cryptography and Data Assurance"
                self.set_field(5)
            elif self.num == 533:
                self.title = "Distributed Computing"
                self.set_field(8)
            elif self.num == 537:
                self.title = "Network and Internet Security"
                self.set_field(8)
                self.set_field(5)
            elif self.num == 538:
                self.title = "Security in Emerging Wireless and Mobile Networks"
                self.set_field(8)
                self.set_field(5)
            elif self.num == 552:
                self.title = "Topics in Rendering"
                self.set_field(11)
            elif self.num == 553:
                self.title = "Software Architecture"
                self.set_field(2)
            elif self.num == 555:
                self.title = "Evaluating Software Design"
                self.set_field(2)
            elif self.num == 565:
                self.title = "Research Methods in Software Development"
                self.set_field(2)
            elif self.num == 566:
                self.title = "Software Management"
                self.set_field(2)
            elif self.num == 572:
                self.title = "Evidence-Based Design"
                self.set_field(2)
            elif self.num == 577:
                self.title = "Secure Software Development"
                self.set_field(2)
                self.set_field(5)
            elif self.num == 578:
                self.title = "Vulnerability Analysis and Detection"
                self.set_field(5)
            elif self.num == 579:
                self.title = "Malware and Attack Reverse Engineering"
                self.set_field(5)
            elif self.num == 590:
                self.title = "Special Topics in Computing"
            elif self.num != 515 and self.num != 539:
                print("No title found for: ", end="")
                self.display()
        elif self.dept == "CSSSKL":
            if self.num == 161:
                self.title = "Fundamental Programming Skills"
                self.set_field(0)
            elif self.num == 162:
                self.title = "Programming Methodology Skills"
                self.set_field(0)
        elif self.dept == "BCUSP":
            if self.num == 161:
                self.title = "Fundamentals of Computing"
                self.set_field(0)
            elif self.num == 162:
                self.title = "Programming Methodology"
                self.set_field(0)

        else:
            print("No title could be found for:", self.num, end="\t")
            self.display()

#    Sets the field for desired expertise
#   0:programming

    def set_field(self, num):
        self.field.append( g.FIELDS[num])


"""
Faculty expertise:
    Programming
    Scientific Computing
    Software Engineering
    Operating Systems
    Hardware
    Cybersecurity
    Writing
    Databases
    Networking
    Teaching
    Computer Engineering
    Graphics
"""


