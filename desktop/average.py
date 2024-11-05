# Problem 2: Create a program that computes for a student’s final grade as the average of three marks. 
# Determine if the student “passed” (≥55) or “failed” (<55) the course.
count = 3
grades = [float(input("Grade: ")) for i in range(count)]

sum = 0
for grade in grades:
    sum += grade
average = sum/count
print("The average of the grade is", round(average))

if average >= 55:
    print("Passed")
else:
    print("Failed")