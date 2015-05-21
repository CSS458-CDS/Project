"""
This file provides the method to build the faculty.
"""
import faculty as f
import globals as g
from openpyxl.reader.excel import load_workbook

"""---------------------------------------
Creates faculty objects from a text file fileName
Pre:
    Using a file formatted exactly like list_of_faculty.xlsx
    No professor classes have been made
Post:
    Faculty classes have been generated with relevant data
File format:
    Column A = Last name
    Column B = Full-time status
    Column C = Number of classes
    Column D = Number of students advised
    Column E = Expertise 1
    Column F = Expertise 2 (if available)
    Column G = Expertise 3 (if available)
"""
def buildFaculty(fileName=g.FACULTY_FILE):

    wb = load_workbook(fileName)
    ws = wb.active
    
    # Build faculty from first readable row to last
    for row in range(g.FACULTY_FILE_FIRST, g.FACULTY_FILE_LAST):
        if ws["A"+str(row)] is not None and row > 4:  # Rows > 4 in the file have relevant data
            lastName = ws["A"+str(row)].value
            
            if ws["B"+str(row)].value == 'Y':
                fullTime = 1
            else:
                fullTime = 0
                
            numClasses = ws["C"+str(row)].value + 0.
            studentsAdvised = ws["D"+str(row)].value
            
            expertise = [ws["E"+str(row)].value]
            
            if ws["F"+str(row)].value != None:
                expertise.append(ws["F"+str(row)].value)
            if ws["G"+str(row)].value != None:
                expertise.append(ws["G"+str(row)].value)
