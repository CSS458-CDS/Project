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
            studentsAdvised: how many students are being advised currently by the faculty member
            expertise: list of subjects faculty member is an expert in
            
            salary = yearly salary of faculty member
            partTimeRatio = number between 0 and 1 that determines what fraction of full time pay a part time
                            faculty member will earn as salary
            
            salaryRatio = final number used to determine salary, based on whether the faculty member is full time or not
            
            currentCourses = list of course numbers for the courses being taught currently by the faculty member
    """
    
    def __init__(self, lName, fullTimeStatus, numClassesTaught, numStudentsAdvised, expertiseList):
        
        self.firstName = None
        self.lastName = lName
        self.age = None
        
        self.timeTeaching = None
        self.hireDate = [None, None, None] # In the format of Month, Day, Year (all integers, like [5, 23, 2015])
        
        self.fullTime = fullTimeStatus 
        self.numClasses = numClassesTaught
        self.studentsAdvised = numStudentsAdvised
        self.expertise = expertiseList
        
        self.salary = None
        self.partTimeRatio = .5 # Used to determine how much salary a faculty member makes on part time
        
        if fullTimeStatus == 'Y':
            self.salaryRatio = 1.
        else: # 'N'
            self.salaryRatio = self.partTimeRatio
            
        self.currentCourses = [] # List of currently taught courses
        
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
