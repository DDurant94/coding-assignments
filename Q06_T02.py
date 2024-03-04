'''
Task 2: Perfect Square Checker
Given a number, determine if it's a perfect square (like 1, 4, 9, 16, …). Hint: You might need the exponentiation operator for this.
'''

num = float(input("Give me a number! "))
perfect_square = num  ** float(0.5)  # Putting the number to the 1/2 power to get the square root(it is the same as writing square root). Than taking that number to the second power to see if it = the number we put in. That will tell us if it is a perfect square.

if perfect_square **2== num:
    print("Perfect square")
else:
    print("Not a perfect square")    

print(perfect_square)




