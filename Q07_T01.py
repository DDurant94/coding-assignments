'''
7. Exploring Logical Operations and Precedence
Objective:
The aim of this assignment is to grasp the concept of logical operations and understand how operator precedence can affect the outcome of an operation.

Task
Task 1: Simple Logic Puzzles
Given a set of True or False values, use the AND, OR, and NOT operators to come up with a desired True or False outcome.
'''
# Made something that will look to see if you are making a rectangle or a square.
x = int(input("Enter a number! "))
y = int(input("Enter a second number! "))


if x <= 0 or y <= 0: 
  print("We need to make a square or rectangle!")
elif x == y:
  print("You are a square!")
else: x > y or y > x
print("We are a rectangle!")  
# saying wow that is going to be a big square or a rectangle
if x and y >= 10:
  print ("wow that us a big shape")
else: x and y <= 9
print ("This a normal size shape!")

if x >= 0:
  print(not x) # I understand how to use a not operator. I am not so sure I know when it would be useful and when it wouldn't be. That is something that I plan to really dive deeper into.
else: y >=0
print(not y)

