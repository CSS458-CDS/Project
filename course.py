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
    """
    def __init__(self, quarter=-1, courseNum=None, time=None, day=None, cap=None):
        self.requirement = None
        self.taughtBy = None
        self.field = "Default Field"
        self.section = -1
        self.dept = "None"
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
        else:
            self.num = -1
            self.meetingDays = -1
            self.capacity = -1
            self.time = -1



    def display(self):
        print(self.dept, self.num, self.section, "\t", self.meetingDays, "\t", self.capacity, "\t", self.time)
        return
    """
    Use the course num to navigate a series of if statements to find the string title of the course.
    Pre: Course has no title
    Post: Course now has a title

    515: Doesnt seem to be offered
    205/405: Women in stem
    """
    def getTitle(self):
        self.num = int(self.num)
        if self.dept == "CSS":
            if self.num == 107:
                self.title = "Introduction to Programming through Animated Storytelling"
            elif self.num == 161:
                self.title = "Fundamentals Of Computing"
            elif self.num == 162:
                self.title = "Programming Methodology"
            elif self.num == 211:
                self.title = "Computers and Society"
            elif self.num == 225:
                self.title = "Physics and Chemistry of Computer Components and Their Manufacture"
            elif self.num == 290:
                self.title = "Topics in Computing"
            elif self.num == 295:
                self.title = "K-12 Computing Education"
            elif self.num == 301:
                self.title = "Technical Writing"
            elif self.num == 310:
                self.title = "Information Assurance and Cyber Security"
            elif self.num == 332:
                self.title = "Programming Issues with Object-Oriented Languages"
            elif self.num == 337:
                self.title = "Secure Systems"
            elif self.num == 341:
                self.title = "Fundamentals of Programming Theory and Applications"
            elif self.num == 342:
                self.title = "Data Structures, Algorithms, and Discrete Mathematics I"
            elif self.num == 343:
                self.title = "Data Structures, Algorithms, and Discrete Mathematics II"
            elif self.num == 350:
                self.title = "Management Principles for Computing Professionals"
            elif self.num == 360:
                self.title = "Software Engineering"
            elif self.num == 370:
                self.title = "Analysis and Design"
            elif self.num == 371:
                self.title = "The Business of Technology"
            elif self.num == 383:
                self.title = "Bioinformatics"
            elif self.num == 385:
                self.title = "Introduction to Game Development"
            elif self.num == 405:
                self.title = "Women in STEM Seminar: Career/Professional Life"
            elif self.num == 411:
                self.title = "Computing Technology and Public Policy"
            elif self.num == 415:
                self.title = "Emerging Topics in Information Assurance and Cybersecurity"
            elif self.num == 421:
                self.title = "Introduction to Hardware and Operating Systems"
            elif self.num == 422:
                self.title = "Hardware and Computer Organization"
            elif self.num == 427:
                self.title = "Introduction to Embedded Systems"
            elif self.num == 428:
                self.title = "Advanced Embedded Systems"
            elif self.num == 430:
                self.title = "Operating Systems"
            elif self.num == 432:
                self.title = "Network Design"
            elif self.num == 434:
                self.title = "Parallel and Distributed Computing"
            elif self.num == 448:
                self.title = "Introduction to Compilers"
            elif self.num == 451:
                self.title = "3-D Computer Graphics"
            elif self.num == 455:
                self.title = "Introduction to Computational Science and Scientific Programming"
            elif self.num == 457:
                self.title = "Multimedia and Signal Computing"
            elif self.num == 458:
                self.title = "Fundamentals of Computer Simulation Theory and Application"
            elif self.num == 473:
                self.title = "Entrepreneurship Seminar"
            elif self.num == 474:
                self.title = "Product Development Lab"
            elif self.num == 475:
                self.title = "Database Systems"
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
            elif self.num == 502:
                self.title = "Data Structures and Object-Oriented Programming II"
            elif self.num == 503:
                self.title = "Systems Programming"
            elif self.num == 506:
                self.title = "Software Development Processes"
            elif self.num == 507:
                self.title = "Software Modeling Techniques"
            elif self.num == 508:
                self.title = "Software Testing and Quality"
            elif self.num == 514:
                self.title = "Security, Policy, Ethics, and the Legal Environment"
            elif self.num == 517:
                self.title = "Information Assurance and the Secure Development Lifecycle"
            elif self.num == 519:
                self.title = "Incident Response and Recovery"
            elif self.num == 527:
                self.title = "Cryptography and Data Assurance"
            elif self.num == 533:
                self.title = "Distributed Computing"
            elif self.num == 537:
                self.title = "Network and Internet Security"
            elif self.num == 538:
                self.title = "Security in Emerging Wireless and Mobile Networks"
            elif self.num == 552:
                self.title = "Topics in Rendering"
            elif self.num == 553:
                self.title = "Software Architecture"
            elif self.num == 555:
                self.title = "Evaluating Software Design"
            elif self.num == 565:
                self.title = "Research Methods in Software Development"
            elif self.num == 566:
                self.title = "Software Management"
            elif self.num == 572:
                self.title = "Evidence-Based Design"
            elif self.num == 577:
                self.title = "Secure Software Development"
            elif self.num == 578:
                self.title = "Vulnerability Analysis and Detection"
            elif self.num == 579:
                self.title = "Malware and Attack Reverse Engineering"
            elif self.num == 590:
                self.title = "Special Topics in Computing"
            elif self.num != 515 and self.num != 539:
                print("No title found for: ", end="")
                self.display()
        elif self.dept == "CSSSKL":
            if self.num == 161:
                self.title = "Fundamental Programming Skills"
            elif self.num == 162:
                self.title = "Programming Methodology Skills"
        elif self.dept == "BCUSP":
            if self.num == 161:
                self.title = "Fundamentals of Computing"
            elif self.num == 162:
                self.title = "Programming Methodology"

        else:
            self.display()

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

