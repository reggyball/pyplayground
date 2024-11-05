# ACTIVITY 3 - GWA CALCULATOR

# BONUS ITEMS - FUNCTIONS THAT CHECK VALIDITY OF USER INPUTS

# Checks validity of course_name, should not be an empty string or space
def valid_coursename(course_name, prompt):
    course_name = course_name.strip()
    while course_name == "":
        print("COURSE NAME MUST HAVE A VALUE")
        course_name = input(prompt)
        course_name = course_name.strip()
    return course_name

# Checks validity of raw_grade, should not be numeric, 0-100
#need to replace first instance of "." with an empty string to allow isnumeric() check decimals
def valid_rawgrade(raw_grade, prompt):
    while not((raw_grade.replace(".", "", 1).isnumeric()) and (float(raw_grade) >= 0 and float(raw_grade) <= 100)):
        print("GRADE MUST BE NUMERIC FORMAT, 0-100")
        raw_grade = input(prompt)
    return float(raw_grade)

# Checks validity of units, should be among the indicated accepted values
def valid_units(units, prompt):
    allow_units = [1.0, 2.0, 3.0, 5.0]
    while not(units.replace(".", "", 1).isnumeric() and float(units) in allow_units):
        print("ENTER ONLY VALID UNITS (1.0, 2.0, 3.0, 5.0)")
        units = input(prompt)
    return float(units)

# OBTAIN USER INPUTS
course_name1 = input("Enter course #1: ")
course_name1 = valid_coursename(course_name1, "Enter course #1: ")

raw_grade1 = input("Enter the grade for " + course_name1 + ": ")
raw_grade1 = valid_rawgrade(raw_grade1, "Enter the grade for " + course_name1 + ": ")

units1 = input("Enter the number of units for " + course_name1 + ": ")
units1 = valid_units(units1, "Enter the number if units for " + course_name1 + ": ")

print("")

course_name2 = input("Enter course #2: ")
course_name2 = valid_coursename(course_name2, "Enter course #2: ")

raw_grade2 = input("Enter the grade for " + course_name2 + ": ")
raw_grade2 = valid_rawgrade(raw_grade2, "Enter the grade for " + course_name2 + ": ")

units2 = input("Enter the number of units for " + course_name2 + ": ")
units2 = valid_units(units2, "Enter the number if units for " + course_name2 + ": ")

print("")

course_name3 = input("Enter course #3: ")
course_name3 = valid_coursename(course_name3, "Enter course #3: ")

raw_grade3 = input("Enter the grade for " + course_name3 + ": ")
raw_grade3 = valid_rawgrade(raw_grade3, "Enter the grade for " + course_name3 + ": ")

units3 = input("Enter the number of units for " + course_name3 + ": ")
units3 = valid_units(units3, "Enter the number if units for " + course_name3 + ": ")

print("")

course_name4 = input("Enter course #4: ")
course_name4 = valid_coursename(course_name4, "Enter course #4: ")

raw_grade4 = input("Enter the grade for " + course_name4 + ": ")
raw_grade4 = valid_rawgrade(raw_grade4, "Enter the grade for " + course_name4 + ": ")

units4 = input("Enter the number of units for " + course_name4 + ": ")
units4 = valid_units(units4, "Enter the number if units for " + course_name4 + ": ")

print("")

course_name5 = input("Enter course #5: ")
course_name5 = valid_coursename(course_name5, "Enter course #5: ")

raw_grade5 = input("Enter the grade for " + course_name5 + ": ")
raw_grade5 = valid_rawgrade(raw_grade5, "Enter the grade for " + course_name5 + ": ")

units5 = input("Enter the number of units for " + course_name5 + ": ")
units5 = valid_units(units5, "Enter the number if units for " + course_name5 + ": ")

print("")

# CONVERT RAW GRADE TO UP EQUIVALENT GRADE
raw_grade = raw_grade1
if (raw_grade >= 96 and raw_grade <= 100):
    point_grade = 1.0
elif (raw_grade >= 90 and raw_grade < 96):
    point_grade = 1.25
elif (raw_grade >= 85 and raw_grade < 90):
    point_grade = 1.5
elif (raw_grade >= 80 and raw_grade < 85):
    point_grade = 1.75
elif (raw_grade >= 76 and raw_grade < 80):
    point_grade = 2.0
elif (raw_grade >= 72 and raw_grade < 76):
    point_grade = 2.25
elif (raw_grade >= 68 and raw_grade < 72):
    point_grade = 2.50
elif (raw_grade >= 64 and raw_grade < 68):
    point_grade = 2.75
elif (raw_grade >= 60 and raw_grade < 64):
    point_grade = 3.00
else:
    point_grade = 5.00
point_grade1 = point_grade


raw_grade = raw_grade2
if (raw_grade >= 96 and raw_grade <= 100):
    point_grade = 1.0
elif (raw_grade >= 90 and raw_grade < 96):
    point_grade = 1.25
elif (raw_grade >= 85 and raw_grade < 90):
    point_grade = 1.5
elif (raw_grade >= 80 and raw_grade < 85):
    point_grade = 1.75
elif (raw_grade >= 76 and raw_grade < 80):
    point_grade = 2.0
elif (raw_grade >= 72 and raw_grade < 76):
    point_grade = 2.25
elif (raw_grade >= 68 and raw_grade < 72):
    point_grade = 2.50
elif (raw_grade >= 64 and raw_grade < 68):
    point_grade = 2.75
elif (raw_grade >= 60 and raw_grade < 64):
    point_grade = 3.00
else:
    point_grade = 5.00
point_grade2 = point_grade

raw_grade = raw_grade3
if (raw_grade >= 96 and raw_grade <= 100):
    point_grade = 1.0
elif (raw_grade >= 90 and raw_grade < 96):
    point_grade = 1.25
elif (raw_grade >= 85 and raw_grade < 90):
    point_grade = 1.5
elif (raw_grade >= 80 and raw_grade < 85):
    point_grade = 1.75
elif (raw_grade >= 76 and raw_grade < 80):
    point_grade = 2.0
elif (raw_grade >= 72 and raw_grade < 76):
    point_grade = 2.25
elif (raw_grade >= 68 and raw_grade < 72):
    point_grade = 2.50
elif (raw_grade >= 64 and raw_grade < 68):
    point_grade = 2.75
elif (raw_grade >= 60 and raw_grade < 64):
    point_grade = 3.00
else:
    point_grade = 5.00
point_grade3 = point_grade


raw_grade = raw_grade4
if (raw_grade >= 96 and raw_grade <= 100):
    point_grade = 1.0
elif (raw_grade >= 90 and raw_grade < 96):
    point_grade = 1.25
elif (raw_grade >= 85 and raw_grade < 90):
    point_grade = 1.5
elif (raw_grade >= 80 and raw_grade < 85):
    point_grade = 1.75
elif (raw_grade >= 76 and raw_grade < 80):
    point_grade = 2.0
elif (raw_grade >= 72 and raw_grade < 76):
    point_grade = 2.25
elif (raw_grade >= 68 and raw_grade < 72):
    point_grade = 2.50
elif (raw_grade >= 64 and raw_grade < 68):
    point_grade = 2.75
elif (raw_grade >= 60 and raw_grade < 64):
    point_grade = 3.00
else:
    point_grade = 5.00
point_grade4 = point_grade


raw_grade = raw_grade5
if (raw_grade >= 96 and raw_grade <= 100):
    point_grade = 1.0
elif (raw_grade >= 90 and raw_grade < 96):
    point_grade = 1.25
elif (raw_grade >= 85 and raw_grade < 90):
    point_grade = 1.5
elif (raw_grade >= 80 and raw_grade < 85):
    point_grade = 1.75
elif (raw_grade >= 76 and raw_grade < 80):
    point_grade = 2.0
elif (raw_grade >= 72 and raw_grade < 76):
    point_grade = 2.25
elif (raw_grade >= 68 and raw_grade < 72):
    point_grade = 2.50
elif (raw_grade >= 64 and raw_grade < 68):
    point_grade = 2.75
elif (raw_grade >= 60 and raw_grade < 64):
    point_grade = 3.00
else:
    point_grade = 5.00
point_grade5 = point_grade


# CALCULATE GWA AND ROUND TO TWO UNITS
units_total = (units1 + units2 + units3 + units4 + units5)
GWA = ((point_grade1 * units1) + (point_grade2 * units2) + (point_grade3 * units3) + (point_grade4 * units4) + (point_grade5 *units5))/units_total
GWA = (GWA*100) + 0.5
Final_GWA = int(GWA)/100

# TABULATE SUMMARY 
print("Here's a summary of your grades this semester: ")
print("{:<10} {:<10} {:<10} {:<10}".format("Course", "Units", "Raw Grade", "UP Eq Grade"))
print("{:<10} {:<10} {:<10} {:<10}".format(course_name1, units1, raw_grade1, point_grade1))
print("{:<10} {:<10} {:<10} {:<10}".format(course_name2, units2, raw_grade2, point_grade2))
print("{:<10} {:<10} {:<10} {:<10}".format(course_name3, units3, raw_grade3, point_grade3))
print("{:<10} {:<10} {:<10} {:<10}".format(course_name4, units4, raw_grade4, point_grade4))
print("{:<10} {:<10} {:<10} {:<10}".format(course_name5, units5, raw_grade5, point_grade5))

print("")

# DISPLAY FINAL COMPUTED GWA
print("Your GWA is", Final_GWA)