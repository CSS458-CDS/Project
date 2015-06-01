import sys
import globals as g
from faculty import faculty

"""
This course provides methods necessary for building a schedule for one faculty member that does not conflict with
other faculty members' schedules, and reflects the expertise of the faculty member in question.
The courses are sorted into 3 categories for each member: high priority, medium priority, and low priority. 
High priority courses are the first courses to be considered when building a schedule for a faculty member. For example,
"Secure Systems" (listed as 337) is a high priority course for a faculty member who is an expert in Cybersecurity.
Medium priority courses are dictated mainly by the prevalence of the three expertise elements "Programming", "Scientific
Computing", and "Scientific Engineering". These are the most prolific areas of expertise and so there are many faculty
members available for courses in these fields. If there are no courses available to teach in high priority, the medium
priority list will be searched instead.
Low priority courses start as the entire collection of courses (see populateLowPrio()). As the algorithm finds courses
and sorts them into high and medium priorities, these same courses are removed from low priority. At the end there should
remain a handful of courses. These courses are considered for a faculty member's schedule if nothing is available from
high and medium priority, and the faculty member is needed to teach one or more of these courses.
This course is still WIP. The following areas are still unfinished at the time of this commit:
- Building the faculty members' schedules and checking them against one another
- May change low priority course conditions
- Testing - lots of testing
"""

# If using this class from a different class, call driver(), not main().
# Main includes testing stuff; it won't be touched unless you're running
# facultyCourseScheduler.py alone.
def main():
    
    listOfFaculty = g.allFaculty
    
    buildSchedule(listOfFaculty, g.AUTCAT, 0)
    buildSchedule(listOfFaculty, g.WINCAT, 1)
    buildSchedule(listOfFaculty, g.SPRCAT, 2)
    buildSchedule(listOfFaculty, g.SUMCAT, 3)

# quarter = 0,1,2,3 depending on what quarter is currently being worked with.
def buildSchedule(listOfFaculty, coursesToTeach, quarter):
    for i in range(0, len(listOfFaculty)):
        listOfFaculty[i].setCurrentlyTeaching(0)
    
    steps = 0
    
    # Assign high/med/low priority courses for each faculty member
    while steps < len(coursesToTeach):
        for i in range(0, len(listOfFaculty)):
            if listOfFaculty[i].getCurrentlyTeaching() < listOfFaculty[i].getNumClasses():
                courseList = prioritizeCourses(listOfFaculty[i], quarter)
                newCourse = scheduleCourses(listOfFaculty[i], courseList, coursesToTeach, quarter)
                
                # Was a faculty assigned to a course? If so, increment currentlyTeaching for faculty
                if newCourse != 000:
                    listOfFaculty[i].setCurrentlyTeaching(listOfFaculty[i].getCurrentlyTeaching() + 1)
                    
                steps += 1    
        

def prioritizeCourses(fac, quarter):
    highPrio = [] # Designates courses that the faculty member is exceptional in
    medPrio = [] # Designates courses that the faculty member can teach
    lowPrio = [] # Designates courses that the faculty member should not teach or
                 # are outside of their range of expertise
    
    populateLowPrio(lowPrio)
    
    listOfCatalogs = [g.AUTCAT, g.WINCAT, g.SPRCAT, g.SUMCAT]
    
    # 1. Loop through every course in that quarter's catalog
    # 2. Check if that course's expertise field matches with the faculty class's
    # 3a. If so, add to high priority list of medium priority list, depending on field
    # 3b. Also, add depending on relevant quarter, determined by listOfCatalogs[quarter][i]
    # 4. If not, continue on to the next expertise if statement.
    for i in range(0, len(listOfCatalogs[quarter])):
        if "Teaching" in listOfCatalogs[quarter][i].getFieldList() and "Teaching" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Writing" in listOfCatalogs[quarter][i].getFieldList() and "Writing" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Graphics" in listOfCatalogs[quarter][i].getFieldList() and "Graphics" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Cybersecurity" in listOfCatalogs[quarter][i].getFieldList() and "Cybersecurity" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Networking" in listOfCatalogs[quarter][i].getFieldList() and "Networking" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Operating Systems" in listOfCatalogs[quarter][i].getFieldList() and "Operating Systems" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Databases" in listOfCatalogs[quarter][i].getFieldList() and "Databases" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Hardware" in listOfCatalogs[quarter][i].getFieldList() and "Hardware" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in highPrio:
                highPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in medPrio:
                medPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Programming" in listOfCatalogs[quarter][i].getFieldList() and "Programming" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in medPrio:
                medPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Scientific Engineering" in listOfCatalogs[quarter][i].getFieldList() and "Scientific Engineering" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in medPrio:
                medPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Scientific Computing" in listOfCatalogs[quarter][i].getFieldList() and "Scientific Computing" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in medPrio:
                medPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())
        if "Software Engineering" in listOfCatalogs[quarter][i].getFieldList() and "Software Engineering" in fac.getExpertise():
            if listOfCatalogs[quarter][i].getCourseNum() not in medPrio:
                medPrio.append(listOfCatalogs[quarter][i].getCourseNum())
            if listOfCatalogs[quarter][i].getCourseNum() in lowPrio:
                lowPrio.remove(listOfCatalogs[quarter][i].getCourseNum())

    return [lowPrio, medPrio, highPrio]
    
def scheduleCourses(curFac, courseList, coursesToTeach, quarter):
    for i in range (0, len(coursesToTeach)):
        for j in range(0, len(courseList[2])): # High priority search
            if coursesToTeach[i].getCourseNum() == courseList[2][j] and coursesToTeach[i].getCourseNum() != None \
            and courseList[2][j] != None and coursesToTeach[i].getTaughtBy == None:
                coursesToTeach[i].setTaughtBy(curFac)
                if quarter == 0:
                    g.AUTCAT[i].setTaughtBy(curFac)
                elif quarter == 1:
                    g.WINCAT[i].setTaughtBy(curFac)
                elif quarter == 2:
                    g.SPRCAT[i].setTaughtBy(curFac)
                else:
                    g.SUMCAT[i].setTaughtBy(curFac)
                return coursesToTeach[i].getCourseNum()
                
    for i in range (0, len(coursesToTeach)):
        for j in range(0, len(courseList[1])): # Medium priority search
            if coursesToTeach[i].getCourseNum() == courseList[1][j] and coursesToTeach[i].getCourseNum() != None \
                and courseList[1][j] != None and coursesToTeach[i].getTaughtBy == None:
                coursesToTeach[i].setTaughtBy(curFac)
                if quarter == 0:
                    g.AUTCAT[i].setTaughtBy(curFac)
                elif quarter == 1:
                    g.WINCAT[i].setTaughtBy(curFac)
                elif quarter == 2:
                    g.SPRCAT[i].setTaughtBy(curFac)
                else:
                    g.SUMCAT[i].setTaughtBy(curFac)
                return coursesToTeach[i].getCourseNum()
                
    return 000

# Append every course to the lowPrio list        
def populateLowPrio(lowPrio):
    lowPrio.append(107) # Introduction to Programming through Animated Storytelling
    lowPrio.append(161) # Fundamentals Of Computing
    lowPrio.append(162) # Programming Methodology
    lowPrio.append(211) # Computers and Society
    lowPrio.append(225) # Physics and Chemistry of Computer Components and Their Manufacture
    lowPrio.append(290) # Topics in Computing
    lowPrio.append(295) # K-12 Computing Education
    lowPrio.append(301) # Technical Writing
    lowPrio.append(310) # Information Assurance and Cyber Security
    lowPrio.append(332) # Programming Issues with Object-Oriented Languages
    lowPrio.append(337) # Secure Systems
    lowPrio.append(341) # Fundamentals of Programming Theory and Applications
    lowPrio.append(342) # Data Structures, Algorithms, and Discrete Mathematics I
    lowPrio.append(343) # Data Structures, Algorithms, and Discrete Mathematics II
    lowPrio.append(350) # Management Principles for Computing Professionals
    lowPrio.append(360) # Software Engineering
    lowPrio.append(370) # Analysis and Design
    lowPrio.append(371) # The Business of Technology
    lowPrio.append(383) # Bioinformatics
    lowPrio.append(385) # Introduction to Game Development
    lowPrio.append(405) # Women in STEM Seminar: Career/Professional Life
    lowPrio.append(411) # Computing Technology and Public Policy
    lowPrio.append(415) # Emerging Topics in Information Assurance and Cybersecurity
    lowPrio.append(421) # Introduction to Hardware and Operating Systems
    lowPrio.append(422) # Hardware and Computer Organization
    lowPrio.append(427) # Introduction to Embedded Systems
    lowPrio.append(428) # Advanced Embedded Systems
    lowPrio.append(430) # Operating Systems
    lowPrio.append(432) # Network Design
    lowPrio.append(434) # Parallel and Distributed Computing
    lowPrio.append(448) # Introduction to Compilers
    lowPrio.append(451) # 3-D Computer Graphics
    lowPrio.append(455) # Introduction to Computational Science and Scientific Programming
    lowPrio.append(457) # Multimedia and Signal Computing
    lowPrio.append(458) # Fundamentals of Computer Simulation Theory and Application
    lowPrio.append(473) # Entrepreneurship Seminar
    lowPrio.append(474) # Product Development Lab
    lowPrio.append(475) # Database Systems
    lowPrio.append(480) # 480 Principles of Human-Computer Interaction
    lowPrio.append(490) # Special Topics in Computing and Software Systems
    lowPrio.append(495) # Applied Computing Internship
    lowPrio.append(496) # Applied Computing Capstone
    lowPrio.append(497) # Computer Science and Software Engineering Capstone
    lowPrio.append(498) # Independent Study
    lowPrio.append(499) # Undergraduate Research
    lowPrio.append(501) # Data Structures and Object-Oriented Programming I
    lowPrio.append(502) # Data Structures and Object-Oriented Programming II
    lowPrio.append(503) # Systems Programming
    lowPrio.append(506) # Software Development Processes
    lowPrio.append(507) # Software Modeling Techniques
    lowPrio.append(508) # Software Testing and Quality
    lowPrio.append(514) # Security, Policy, Ethics, and the Legal Environment
    lowPrio.append(517) # Information Assurance and the Secure Development Lifecycle
    lowPrio.append(519) # Incident Response and Recovery
    lowPrio.append(527) # Cryptography and Data Assurance
    lowPrio.append(533) # Distributed Computing
    lowPrio.append(537) # Network and Internet Security
    lowPrio.append(538) # Security in Emerging Wireless and Mobile Networks
    lowPrio.append(552) # Topics in Rendering
    lowPrio.append(553) # Software Architecture
    lowPrio.append(555) # Evaluating Software Design
    lowPrio.append(565) # Research Methods in Software Development
    lowPrio.append(566) # Software Management
    lowPrio.append(572) # Evidence-Based Design
    lowPrio.append(577) # Secure Software Development
    lowPrio.append(578) # Vulnerability Analysis and Detection
    lowPrio.append(579) # Malware and Attack Reverse Engineering
    lowPrio.append(590) # Special Topics in Computing

if __name__ == "__main__": # Testing - points to this course's "main" method, so to speak
    sys.exit(main())
