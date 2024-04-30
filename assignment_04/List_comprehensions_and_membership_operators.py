'''
4. List Comprehensions and Membership Operators
Objective:
The aim of this assignment is to practice using list comprehensions and membership operators in Python.

Problem Statement:
You have a list of numbers, and you'd like to generate a new list based on certain conditions.

Task 1: Given the list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Use a list comprehension to create a new list containing only even numbers.

Task 2: Use a list comprehension to create a new list containing numbers greater than 5.

Task 3: Check if the number 7 is in the original numbers list.
'''

# Task one
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#even_numbers = [x for x in numbers if x % 2 == 0 ]
print(even_numbers)
'''

# Task two 
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#nums_larger_than_five = list(filter(lambda x: x > 5, numbers))
nums_larger_than_five = [x for x in numbers if x > 5]
print(nums_larger_than_five)
'''

# Task three

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Checking if 7 is in the list above.
checking_nums = True if 7 in numbers else False
if checking_nums == True:
  print(checking_nums, "7 is in the list above!")
else:
  print("False 7 is not in the list above!")

#if 7 in numbers:
#  print("True 7 is in the list above!")
#else:
#  print("False 7 is not in the list above!")
