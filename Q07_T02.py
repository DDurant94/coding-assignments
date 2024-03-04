'''
Task 2: Validating Calculations
Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match
'''
w = 5
x = 6
y =7
z = 8

print(w + x * y / z) # 10.25 (we took x * y = 42 / z = 5.25 + w = 10.25)
print ((w + x) * y / z) # It is going to be two different answers because of PEMDAS (9.625) (w + x = 11 * y = 77 / 8 = 9.625)
