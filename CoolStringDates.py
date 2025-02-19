# Description: Cool Stuff with Strings and Dates - Digital Employee ID
# Author: Cameron Boyer
# Date(s): February 18, 2025 - February 26, 2025


# Define required libraries.
import datetime


# Define program constants.


# Main program starts here.


CurDate = datetime.datetime.now()

# Gather user inputs.

EmpNameFirst = "John"
EmpNameLast  = "Smith"
Phone     = "1(555)782-4039"

StartDate = "2016-03-14"
BirthDate = "1984-05-09"




# Perform required calculations.
StartDate = datetime.datetime.strptime("2016-03-14", "%Y-%m-%d")
BirthDate = datetime.datetime.strptime("1984-05-09", "%Y-%m-%d")

EmpNum = EmpNameFirst[0] + EmpNameLast[0] + Phone[10:] + StartDate.strftime("%y") + BirthDate.strftime("%y")

EmpAge = int((CurDate - BirthDate).days / 365.25) 

YearsToRetire = 65 - EmpAge
RetireYear  = CurDate.year + YearsToRetire

NextBirthday = datetime.datetime(CurDate.year, BirthDate.month, BirthDate.day)

# If birthday has passed this year, add a year
if CurDate > NextBirthday:
    NextBirthday = datetime.datetime(CurDate.year + 1, BirthDate.month, BirthDate.day)

UntilBirthday = (NextBirthday - CurDate).days

# Display results
print(EmpNum)
print(EmpAge)
print(YearsToRetire)
print(RetireYear)
print(NextBirthday)
print(UntilBirthday)


# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.