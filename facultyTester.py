"""
A quick way to test some key functions in faculty.py
"""

from faculty import faculty

expertList = ["Eating", "Playing vidya"]

prof = faculty("Hawkins", "Y", 12, 5, expertList)

prof.setFirstName("Caleb")

prof.setAge(21)

prof.setHireDate([5, 23, 2015])

prof.setTimeTeaching(5)

prof.setSalary(50000)

prof.display()
