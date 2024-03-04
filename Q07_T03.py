'''
Task 3: Mix and Match
Combine arithmetic, logical, and comparison operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct.
'''
w = 2
x = 3
y = 4
z = 5

if w * x and y * z >= x ** y: # both w * x and y * z have to be great than or equal to x to the y power. In this example that wont happen so it will print the else statement.
  print("x to the y power isn't greater than or equal to both w * x and y * z!")
else:
  print("x to the y power is greater than both w * x and y * z aren't greater!")