import courseDriver
#Name of the file used for building course catalogs
COURSE_FILE = "list_of_classes.xlsx"
FACULTY_FILE = "list_of_faculty.xlsx"
#First line that contains course data in course file
COURSE_FILE_FIRST = 9
#Last Line of relevant information in course file
COURSE_FILE_LAST = 100
# of all the graduated student, the percentage of students becoming master student
MASTER_STUDENT_PERCENT = 0.1

#Course catalog. List of all the courses offered in Autum.
AUTCAT = []
#Course catalog. List of all the courses offered in Winter.
WINCAT = []
#Course catalog. List of all the courses offered in Spring.
SPRCAT = []
#Course catalog. List of all the courses offered in Summer.
SUMCAT = []
#elective Course catalog. List of all the elective courses offered in a year, courses are represented as int
ELCCAT = []

def initialize_globals():
    courseDriver.buildClasses(COURSE_FILE)
