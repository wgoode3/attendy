import json, time, os, shutil
from statistics import mode
import os, re
 
# simple email regex
EMAIL_CHECK = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

# the values used on the attendance sheet
ATTENDANCE_VALUES = ("a", "l", "d", "x", "k")


# reads in the csv sheet, returns a list of dictionaries of student data
# with email and daily attendance status
def read_sheet():
    
    # find the csv in the downloads folder and read it in 
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    ls = os.listdir(downloads_folder)
    SHEET = None
    for file in ls:
        if file.endswith(".csv"):
            file_location = os.path.join(downloads_folder, file)
            with open(file_location) as file:
                SHEET = file.read()
            break

    lines = []
    if SHEET is not None:
        # ugly list comprehension to find just the rows of data with students
        # if index 0 is an email, then it is a student entry to check through
        lines = [line for line in SHEET.splitlines() if EMAIL_CHECK.match(line.split(",")[0])]
    
    # try to work out the current day by finding the last column with attendance data
    current_days = []
    for line in lines:
        data = line.split(",")
        i = len(data) - 1
        while data[i] == "":
            i -= 1
        current_days.append(i)

    # set i to current day index
    # calculated from the index most students have attendance data for
    i = mode(current_days)

    # create an array of student dictionaries
    students = []
    for line in lines:
        data = line.split(",")
        if data[i] != "" and data[i][0].lower() in ATTENDANCE_VALUES:
            student = {"email": data[0], "status": data[i][0].lower()}
        else:
            student = {"email": data[0], "status": "?"}
        students.append(student)

    # delete the csv file from downloads and return the student data
    os.remove(file_location)
    return students