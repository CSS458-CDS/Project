class faculty:
    """
    class faculty
        Members
            firstName: first name of faculty member
            middleName: middle name/initial of faculty member
            lastName: last name of faculty member
            fullTime: determines if faculty member is full-time (1 if yes, 0 if no)
            numClasses: how many classes are being taught by faculty member
            studentsAdvised: how many students are being advised currently by the faculty member
            expertise: list of subjects faculty member is an expert in
    """
    
    def __init__(self, lName, fullTimeStatus, numClassesTaught, numStudentsAdvised, expertiseList):
        
        self.firstName = None
        self.lastName = lName
        
        self.age = None
        self.timeTeaching = None
        
        self.fullTime = fullTimeStatus 
        self.numClasses = numClassesTaught
        self.studentsAdvised = numStudentsAdvised
        
        self.salary = None
        
        self.expertise = expertiseList
        
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
        return self.fullTime
        
    def setTimeTeaching(self, num):
        self.timeTeaching = num
    
    def checkForSabbatical(self):
        return (self.timeTeaching % 7 == 0)
        
    def getSalary(self):
        return self.salary
        
    def setSalary(self, newSalary):
        self.salary = newSalary
