'''
2. Advanced List Methods and Identity Operators
Objective:
The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

Problem Statement:
You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
Find out which students both submitted their assignments and attended the class.

Task 2: Check if the two lists are identical in terms of their content, regardless of order.

Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
'''
# Task one.

'''
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

submitted_attended = submitted + attended
attended_class_and_submitted = [x for x in submitted_attended if submitted_attended.count(x) > 1] #I need to really think about this more of what I am being asked. I stuggled to make this at first. 
print(list(set(attended_class_and_submitted)))

#attended_class_and_submitted = list(set(filter(lambda x: submitted_attended.count(x) > 1, submitted_attended)))
#print(attended_class_and_submitted)
'''


# Task two

'''
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if submitted == attended:
  print("They are the same!")
else:
  print("They are not the same!")
'''

# Task three



submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
#attended.remove("Eve")
#attended.remove("Frank")
#print(attended)

# The names are removed from the list manually, but I am thinking that you have to be able to do it in a better way.

submitted_attended = submitted + attended

#                       return(x) for  x  in  the  list       if  list            count x is    greater than 1
#attended_class_and_submitted = [x for x in submitted_attended if submitted_attended.count(x) > 1]

# this is the same thing as above just with the filter instead of writing the whole problem out.
attended_class_and_submitted = list(set(filter(lambda x: submitted_attended.count(x) > 1, submitted_attended)))

#                                remove from list (i) for i in   list    if i is  not in (different list)  is True
#attended_class_and_didnt_submit = [attended.remove(i) for i in attended if i not in attended_class_and_submitted]
#print(attended)

# same as above but using filter. 
attended_class_and_didnt_submit = list(filter(lambda a: attended.remove(a) if a not in attended_class_and_submitted else None , attended))
print(attended)
