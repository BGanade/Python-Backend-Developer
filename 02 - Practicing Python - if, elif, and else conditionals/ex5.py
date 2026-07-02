""" Carlos wants to monitor his monthly budget to avoid overspending. He has set a 
spending limit of R$ 3,000.00 and needs a program to help track his expenses. The 
program should take the total expenses incurred as input and indicate whether he has 
exceeded the limit or is still within budget. """

BUDGET_LIMIT = 3000

spend = float(input("Enter your total expenses this month: "))

if spend > BUDGET_LIMIT:
    print(
        f"You have exceeded the budget limit by "
        f"R${spend - BUDGET_LIMIT:.2f}."
    )
else:
    print(
        f"You still have "
        f"R${BUDGET_LIMIT - spend:.2f} remaining in your budget."
    )
