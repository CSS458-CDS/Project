#Name of the file used for building course catalogs
COURSE_FILE = "list_of_classes.xlsx"
FACULTY_FILE = "list_of_faculty.xlsx"
#First line that contains course data in course file
COURSE_FILE_FIRST = 9
#Last Line of relevant information in course file
COURSE_FILE_LAST = 100
COURSE_TITLE_PRINT_LENGTH = 20
# of all the graduated student, the percentage of students becoming master student
MASTER_STUDENT_PERCENT = 0.1
#This list contains the classes that are considered core to the major.
#Any classes that are not in this list are considered electives.
CORE_CLASSES = {161, 162, 301, 342, 343, 350, 360, 370, 422, 430}

#Course catalog. List of all the courses offered in Autum.
AUTCAT = []
#Course catalog. List of all the courses offered in Winter.
WINCAT = []
#Course catalog. List of all the courses offered in Spring.
SPRCAT = []
#Course catalog. List of all the courses offered in Summer.
SUMCAT = []
#elective Course catalog. List of all the elective courses offered in a year, courses are represented as int
ALL_ELECTIVES = []
#Dictionary to get the field from a number
FIELDS = {0:"Programming", 1:"Scientific Computing", 2:"Software Engineering",
        3:"Operating Systems", 4:"Hardware", 5:"Cyber Security", 6:"Writing",
        7:"Databases", 8:"Networking", 9:"Teaching", 10:"Computer Engineering",
        11:"Graphics", 12:"Any"}
def initialize_globals():
    import courseDriver as cd
    cd.buildClasses()
    get_all_electives()

def get_all_electives():
    for i in range(len(AUTCAT)):
        if AUTCAT[i].num not in ALL_ELECTIVES:
            ALL_ELECTIVES.append(AUTCAT[i].num)
    for i in range(len(WINCAT)):
        if WINCAT[i].num not in ALL_ELECTIVES:
            ALL_ELECTIVES.append(WINCAT[i].num)
    for i in range(len(SPRCAT)):
        if SPRCAT[i].num not in ALL_ELECTIVES:
            ALL_ELECTIVES.append(SPRCAT[i].num)
    for i in range(len(SUMCAT)):
        if SUMCAT[i].num not in ALL_ELECTIVES:
            ALL_ELECTIVES.append(SUMCAT[i].num)



