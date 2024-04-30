'''
1. Python List Transformation
Objective:
The aim of this assignment is to practice advanced list operations and transformations.

Problem Statement:
You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
Sort the grades in descending order and display the sorted list.

Task 2: Calculate the average grade and display it.

Task 3: Replace any grade below 80 with the value Failed.
'''
# Task one. 

'''
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#grades.sort()
#grades.reverse()

#grades.sort(), grades.reverse()

grades.sort(reverse = True)

# I could use any of the three but personally like grades.sort(reverse = True)

print(grades)
'''



# Task two.
'''
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

average_grade = sum(grades) / len(grades)

print(average_grade)
'''


# Task three.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades = ["failed" if x < 80 else x for x in grades]  # Running an if statement inside the list lets me make change to the list.
print(grades)

#lambda x : x < 80, grades