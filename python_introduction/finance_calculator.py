# User monthly Income
monthly_income = float(input("Enter your monthly income: "))

# User montly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses 

# Calculate projected annual savings with interest
projected_savings = monthly_savings * 12 
+ ((monthly_savings * 12 * 0.05)) 

# Print Results
print(f"your monthly savings are ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
