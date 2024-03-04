'''
Task 2: Bank Interest
If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year.
'''


# this is how i would solve the problem where you can enter in any fixed number or fixed interest amount.

savings_account = input("Total amount you want to put in savings? ") # You can add in any fixed amount that you want to caculate on a APR. 
active_savings_account = float(savings_account)
yearly_intrest = input("Percentage rate to be used? ") # you can also put in your fixed interest amount as well.
active_yearly_interest = float(yearly_intrest)
interest_applied = active_yearly_interest / 100 


total_interest_yearly = active_savings_account * interest_applied
print ("$",round(total_interest_yearly, 2), "Is the amount paid at", yearly_intrest, "percent interest a year.")
 
# How I think that you are asking to solve the problem.
'''
savings_account = 200
yearly_intrest = 6.5 / 100
 
interest_paid_out = savings_account * yearly_intrest
print("$", round(interest_paid_out, 2))'''
