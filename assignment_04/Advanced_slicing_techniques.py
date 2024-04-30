'''
3. Advanced Slicing Techniques
Objective:
The aim of this assignment is to master the art of slicing in Python lists.

Problem Statement:
You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
Extract the temperatures for the second week (7 days) of the month.

Task 2: Extract all the temperatures above 100.

Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
'''


# Task one

'''
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# To extract the temp for the second week of the month all 7 days. 

week_two_temps = temperatures[7:14]
print(week_two_temps)
'''

# Task two

'''
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
#                 replace (x) for x in   list       if x is > 99
#temps_over_one_hundred = [x for x in temperatures if x > 99]
#print (temps_over_one_hundred)

# could also do this with knowing the total list and not having to search for those temps

temps_over_one_hundred = temperatures[23:30]
print (temps_over_one_hundred)
'''

# Task three 
# Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

temperatures.reverse()
five_day_temp = temperatures[4:10]

print(five_day_temp)