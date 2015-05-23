class faculty:
    """
    class faculty
        Members
            firstName: first name of faculty member
            lastName: last name of faculty member
            age: age of faculty member
            
            timeTeaching = amount of time having worked as a faculty member
            hireDate = date of hire, in the format of [month, day, year] in ints
            
            fullTime: determines if faculty member is full-time (1 if yes, 0 if no)
            numClasses: how many classes are being taught by faculty member
            currentCourses = list of course numbers for the courses being taught currently by the faculty member
            studentsAdvised: how many students are being advised currently by the faculty member
            expertise: list of subjects faculty member is an expert in
            
            salary = yearly salary of faculty member
            partTimeRatio = number between 0 and 1 that determines what fraction of full time pay a part time
                            faculty member will earn as salary
            
            salaryRatio = final number used to determine salary, based on whether the faculty member is full time or not
    """
    
    def __init__(self, lName, fullTimeStatus, numClassesTaught, numStudentsAdvised, expertiseList):
        
        self.firstName = None
        self.lastName = lName
        self.age = None
        
        self.timeTeaching = None # In years
        self.hireDate = [None, None, None] # In the format of Month, Day, Year (all integers, like [5, 23, 2015])
                                           # ASSUMPTION: if a date is provided, it will be a "complete" date.
        
        self.fullTime = fullTimeStatus 
        self.numClasses = numClassesTaught
        self.currentCourses = [] # List of currently taught courses
        self.studentsAdvised = numStudentsAdvised
        self.expertise = expertiseList
        
        self.salary = None
        self.partTimeRatio = .5 # Used to determine how much salary a faculty member makes on part time
        
        if fullTimeStatus == 'Y':
            self.salaryRatio = 1.
        else: # 'N'
            self.salaryRatio = self.partTimeRatio
            
        
        
    def display(self):
        if self.firstName != None:
            print self.lastName + ", " + self.firstName
        else:
            print self.lastName
        
        if self.age != None:    
            print "Age: " + self.age
            
        if self.timeTeaching != None:
            print "Has been teaching for " + self.timeTeaching + " years"
            
        if self.hireDate[0] != None and self.hireDate[1] != None and self.hireDate[2] != None:
            print "Has taught since " + self.hireDate[0] + " " + self.hireDate[1] + ", " + self.hireDate[2]
            
        print "Full time or part time: ",
        if self.fullTime == 'Y':
            print "full time"
        else:
            print "part time"
            
        print "Number of classes currently teaching: " + self.numClasses
        
        if self.hireDate:
            print "Classes being taught currently: " + self.hireDate
            
        print "Number of students currently advising: " + self.studentsAdvised 
        
        if self.expertise:
            print "Areas of expertise: " + self.expertise
            
        if self.salary:
            print "Yearly salary: " + self.salary
        
    def getNumClasses(self):
        return self.numClasses
        
    def getExpertise(self):
        return self.expertise
        
    def getWholeName(self):
        return self.lastName + ", " + self.firstName + " " + self.middleName
        
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
        
    def getAge(self):
        return self.age
        
    def setAge(self, newAge):
        self.age = newAge
    
    # Returns 1 if Y, 0 if N    
    def getFullTime(self):
        if self.fullTime == 'Y':
            return 1
        else:
            return 0
        
    def setTimeTeaching(self, num):
        self.timeTeaching = num
    
    def checkForSabbatical(self):
        return (self.timeTeaching % 7 == 0)
        
    def getSalary(self):
        return self.salary
        
    def setSalary(self, newSalary):
        self.salary = newSalary * self.salaryRatio

    def getCurrentCourses(self):
        return self.currentCourses

    def getHireDate(self):
        return self.hireDate
        
    def setHireDate(self, newHireDate):
        self.hireDate = newHireDate
