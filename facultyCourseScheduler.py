import sys
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

def main():
    
    # Listed in order from earliest class to latest class
    coursesToTeach = [332, 478, 432, 107, 337, 343, 342]
    
    schedule = []
    
    # Build list with 5 faculty members
    listOfMembers = []
    newFac1 = faculty("Stark", "Y", 12, 5, ["Programming", "Cybersecurity", "Teaching"])
    newFac2 = faculty("Rogers", "Y", 12, 5, ["Hardware", "Operating Systems"])
    newFac3 = faculty("Banner", "Y", 12, 5, ["Scientific Computing"])
    newFac4 = faculty("Romanoff", "Y", 12, 5, ["Scientific Engineering", "Databases"])
    newFac5 = faculty("Barton", "Y", 12, 5, ["Programming", "Networking"])
    
    listOfMembers.extend((newFac1,newFac2,newFac3,newFac4,newFac5)) # List with 5 faculty members
    
    # Assign high/med/low priority courses for each faculty member
    while len(coursesToTeach) > 0:
        for i in range(0, len(listOfMembers)):
            courseList = prioritizeCourses(listOfMembers[i])
            newCourse = scheduleCourses(courseList, coursesToTeach)
            schedule.append(str(listOfMembers[i].getLastName()) + " is teaching " + str(newCourse))
            
    print(schedule)

def prioritizeCourses(fac):
    highPrio = [] # Designates courses that the faculty member is exceptional in
    medPrio = [] # Designates courses that the faculty member can teach
    lowPrio = [] # Designates courses that the faculty member should not teach or
                 # are outside of their range of expertise
    
    populateLowPrio(lowPrio)
    
    # Below, we deal with specialties of narrower focus; we put these in high
    # priority immediately.   
    
    # Format:
    # courseList = all courses relevant to the field
    # Add these courses to high priority, remove from medium and low
    
    if "Teaching" in fac.getExpertise():
        courseList = [295]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
        if courseList[i] in medPrio:
            medPrio.remove(courseList[i])
        elif courseList[i] in lowPrio:
            lowPrio.remove(courseList[i])
    
    if "Databases" in fac.getExpertise():
        courseList = [478]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
        if courseList[i] in medPrio:
            medPrio.remove(courseList[i])
        elif courseList[i] in lowPrio:
            lowPrio.remove(courseList[i])
            
    if "Writing" in fac.getExpertise():
        courseList = [301,411]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
        if courseList[i] in medPrio:
            medPrio.remove(courseList[i])
        elif courseList[i] in lowPrio:
            lowPrio.remove(courseList[i])
        
    if "Networking" in fac.getExpertise():
        courseList = [432,537,538]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
        if courseList[i] in medPrio:
            medPrio.remove(courseList[i])
        elif courseList[i] in lowPrio:
            lowPrio.remove(courseList[i])
            
    if "Hardware" in fac.getExpertise():
        courseList = [225,421,422,427,428]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
        if courseList[i] in medPrio:
            medPrio.remove(courseList[i])
        elif courseList[i] in lowPrio:
            lowPrio.remove(courseList[i])
        
    if "Operating Systems" in fac.getExpertise():
        courseList = [421,427,428, 430, 448]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
        if courseList[i] in medPrio:
            medPrio.remove(courseList[i])
        elif courseList[i] in lowPrio:
            lowPrio.remove(courseList[i])
            
    if "Cybersecurity" in fac.getExpertise():
        courseList = [337,415,432,514,517,519,527,537,538,577,578,579]
        
        for i in range(len(courseList)):
            if courseList[i] not in highPrio:
                highPrio.append(courseList[i])
                
            if courseList[i] in medPrio:
                medPrio.remove(courseList[i])
            elif courseList[i] in lowPrio:
                lowPrio.remove(courseList[i])
                
    # courseList = all courses relevant to the field
    if "Programming" in fac.getExpertise():
        courseList = [107,161,162,332,341,342,343,360,385,421,422,427,428,430,432,\
                    448,455,458,474,475,501,502,503,506,507,508,533,553,555,565,\
                    566,572,577]
                    
        for i in range(len(courseList)):
            if courseList[i] not in medPrio:
                medPrio.append(courseList[i])
            
            if courseList[i] in lowPrio:
                lowPrio.remove(courseList[i])
                
    if "Scientific Computing" in fac.getExpertise():
        courseList = [107,161,162,211,225,290,332,337,341,342,343,350,360,370,371,\
                    385,411,421,422,427,428,430,432,434,455,458,475,480,490,495,\
                    496,497,498,499,501,502,503,506,507,508,517,533,537,552,553,\
                    555,565,566,577,590]
                    
        for i in range(len(courseList)):
            if courseList[i] not in medPrio:
                medPrio.append(courseList[i])
            
            if courseList[i] in lowPrio:
                lowPrio.remove(courseList[i])
                
    if "Scientific Engineering" in fac.getExpertise():
        courseList = [107,161,162,211,225,290,332,337,341,342,343,350,360,370,371,\
                    385,411,421,422,427,428,430,432,434,455,458,475,480,490,495,\
                    496,497,498,499,501,502,503,506,507,508,517,533,537,552,553,\
                    555,565,566,577,590]
                    
        for i in range(len(courseList)):
            if courseList[i] not in medPrio:
                medPrio.append(courseList[i])
            
            if courseList[i] in lowPrio:
                lowPrio.remove(courseList[i])
            
    print("High priority courses: ", str(highPrio))
    print("Medium priority courses: ", str(medPrio))
    print("Low priority courses: ", str(lowPrio))
    
    return [lowPrio, medPrio, highPrio]
    
def scheduleCourses(courseList, coursesToTeach):
    for i in range (0, len(coursesToTeach)):
        for j in range(0, len(courseList[2])):
            if coursesToTeach[i] == courseList[2][j] and coursesToTeach[i] != None \
            and courseList[2][j] != None:
                dummyCourse = coursesToTeach[i]
                coursesToTeach.remove(coursesToTeach[i])
                return dummyCourse
                
    for i in range (0, len(coursesToTeach)):
        for j in range(0, len(courseList[1])):
            if coursesToTeach[i] == courseList[1][j] and coursesToTeach[i] != None \
                and courseList[1][j] != None:
                dummyCourse = coursesToTeach[i]
                coursesToTeach.remove(coursesToTeach[i])
                return dummyCourse
                
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
