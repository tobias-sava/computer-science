# 23/01/2025

# Check PSET Materials folder > MIT6_100L_F22 for instructions.

yearly_salary = float(input("Enter yearly salary: "))

portion_saved = float(input("Enter portion of salary to be saved (0.1 - 1) with 0.1 representing 10%: "))

cost_of_dream_home = float(input("Enter the cost of house: "))

# constant variables

portion_down_payment = 0.25 # (25%)

amount_saved = 0

r = 0.05 # (5%) / r represents the annual rate

monthly_salary = yearly_salary / 12

months = 0 # stores amount of months required for down payment

down_payment = cost_of_dream_home * portion_down_payment # dream home cost * down payment percentage

# while loop to iterate until amount_saved meets or exceeds the down payment

while amount_saved < down_payment:
  # calculate monthly return on current savings
  amount_saved += amount_saved * (r / 12)
  
  # add monthly savings from salary
  monthly_savings = monthly_salary * portion_saved
  amount_saved += monthly_savings
  
  # increment the months counter
  months += 1

  # no need for exit since while will naturally exit when amt_saved >= down_payment

print(months)

# all 3 manual test cases passed!




