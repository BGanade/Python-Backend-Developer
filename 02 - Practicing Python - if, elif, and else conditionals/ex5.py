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