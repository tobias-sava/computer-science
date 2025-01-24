# Problem Set 1C - Choosing an interest rate
# Name: Tobias Sava
# Date: 24/01/2025
# Time Spent: 20 minutes

# Check PSET Materials folder -> MIT6_100L_F22 for instructions.

# taking input
yearly_salary = float(input("Enter yearly salary: "))

initial_deposit = float(input("Enter your initial deposit amount: $"))

portion_saved = float(input("Enter portion of salary to be saved (0.1 - 1) with 0.1 representing 10%: "))

cost_of_dream_home = float(input("Enter the cost of house: "))

semi_annual_raise = float(input("Enter semi-annual raise amount (0.1 - 1) with 0.1 representing 10%: "))

# constant variables
portion_down_payment = 0.25 # (25%)

down_payment = cost_of_dream_home * portion_down_payment # dream home cost * down payment percentage

def savings_after_3_years(r, yearly_salary):
    """
    Function to calculate savings after 3 years (36 months) given a rate of return r.
    Includes initial deposit and monthly savings with semi-annual raises.
    """
    amount_saved = initial_deposit
    monthly_salary = yearly_salary / 12
    
    for month in range(36):  # 36 months = 3 years
        # calculate monthly return on current savings
        amount_saved += amount_saved * (r / 12)
        
        # add monthly savings from salary
        monthly_savings = monthly_salary * portion_saved
        amount_saved += monthly_savings
        
        # calculate semi-annual raise (every 6 months)
        if (month + 1) % 6 == 0:
            yearly_salary += yearly_salary * semi_annual_raise
            monthly_salary = yearly_salary / 12  # update monthly salary after raise

    return amount_saved


# bisection search variables
low = 0.0
high = 1.0
r = (low + high) / 2.0
steps = 0

# handle special cases
if initial_deposit >= down_payment - 100:
    print("Best savings rate: 0.0")
    print("Steps in bisection search: 0")
else:
    while True:
        steps += 1
        amount_saved = savings_after_3_years(r, yearly_salary)
        
        # check if the savings are within $100 of the down payment
        if abs(amount_saved - down_payment) <= 100:
            break
        
        # adjust bisection search bounds
        if amount_saved < down_payment:
            low = r
        else:
            high = r

        r = (low + high) / 2.0 # recalculate mid-point
        
        # if the interval becomes too small, break
        if high - low < 1e-9:
            r = None
            break

    # output results
    if r is None:
        print("It is not possible to save for the down payment in 3 years.")
    else:
        print(f"Best savings rate: {r}")
        print(f"Steps in bisection search: {steps}")

# all manual tests passed
