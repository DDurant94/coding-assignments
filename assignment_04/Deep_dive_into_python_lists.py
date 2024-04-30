'''
5. Deep Dive into Python Lists
Objective:
The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

Problem Statement:
You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
Filter out students who have grades below 80. Print the name, grade and activiy

Task 2: For the remaining students, add students name in a new list named students_approved

Task 3: Print the list students_approved


Note: that filter(function, iterable) is equivalent to the generator expression 
(item for item in iterable if function(item)) if function is not None and 
(item for item in iterable if item) if function is None.

Note: A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
Syntax
lambda arguments : expression

'''

# Task one
'''
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

#students.remove("Jane")
#grades.remove(78)
#activities.remove("Art")
#print(students,grades,activitie

#zip brings in different lists into a tulpe but i needed to make it back into a list because of an error.
combined_list = list(zip(students,grades,activities))
grades_above_eighty = filter(lambda score: score[1] > 80, combined_list)
print(list(grades_above_eighty))
# I am not sure if this is what is being looked for. I could go in and take out each one manually using list.remove()
'''

# Task two and three

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

#students.remove("Jane")
#grades.remove(78)
#activities.remove("Art")
#print(students,grades,activities)
#students_approved = list(zip(students,grades,activities))
#print(students_approved)

# I tried to complete this in two different ways to try and challenge myself and my abilities. 
combined_list = list(zip(students,grades,activities))
students_approved = filter(lambda score: score[1] > 80, combined_list)
print(list(students_approved))



