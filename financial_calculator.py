"""
START
DISPLAY "investment - to calculate the amount of interest you'll earn on your investment"
DISPLAY "bond - to calculate the amount you'll have to pay on a home loan"

INPUT user_choice (convert to lowercase)

IF user_choice == "investment" THEN
INPUT deposit_amount
INPUT interest_rate (as percentage and convert to decimal)
INPUT number_of_years
INPUT interest_type ("simple" or "compound")

IF interest_type == "simple" THEN
total_amount = deposit_amount * (1 + interest_rate * number_of_years)
DISPLAY total_amount after number_of_years
ELSE IF interest_type == "compound" THEN
total_amount = deposit_amount * (1 + interest_rate) ^ number_of_years
DISPLAY total_amount after number_of_years
ELSE
DISPLAY "Error: please choose 'simple' or 'compound'."

ELSE IF user_choice == "bond" THEN
    INPUT present_value_of_house
    INPUT annual_interest_rate (convert to monthly interest rate)
    INPUT number_of_months

    repayment = (monthly_interest_rate * present_value_of_house) / (1 - (1 + monthly_interest_rate) ^ -number_of_months)
    DISPLAY monthly repayment

ELSE
    DISPLAY "Error: please choose 'investment' or 'bond'."
END
"""



import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")


calculation_choice = input("Please choose 'investment' or 'bond': ").lower()

if calculation_choice == "investment":
    deposit = float(input("Please enter your deposit amount: "))
    interest_rate = float(input("Please enter the interest rate (without %): ")) / 100
    the_number_of_years = round(float(input("Please enter the number of years you plan on investing: ")), 2)
    interest = input("Please choose 'simple' or 'compound': ").lower()

# calculating investment
    if interest == "simple":
        amount = deposit * (1 + interest_rate * the_number_of_years)
        print(f"The amount of money you will receive after {the_number_of_years} years is {amount:.2f}")
    elif interest == "compound":
        amount = deposit * math.pow((1 + interest_rate), the_number_of_years)
        print(f"The amount of money you will receive after {the_number_of_years} years is {amount:.2f}")
    else:
        print("Error: please choose only 'simple' or 'compound'.")

# If user chooses 'bond'
elif calculation_choice == "bond":
    present_value = float(input("Please enter the present value of the house: "))
    the_interest_rate = float(input("Please enter the annual interest rate (without %): ")) / 100 / 12 
    duration_of_the_months = int(input("Please enter the number of months you plan to take to repay the bond: "))
    
    # Calculate bond repayment
    repayment = (the_interest_rate * present_value) / (1 - (1 + the_interest_rate) ** (- duration_of_the_months))
    print(f"Your monthly repayment amount is: {repayment:.2f}")

# Handle invalid input
else:
    print("Error: Please enter either 'investment' or 'bond'.")

