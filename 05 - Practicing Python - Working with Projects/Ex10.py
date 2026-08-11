""" A bank is developing a system for ATMs and needs a program that simulates cash 
withdrawals. The ATM must dispense the requested amount using the smallest possible 
number of bills. The available denominations are: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, 
and R$ 2.

Create a program that asks the user for the withdrawal amount and calculates how many 
bills of each denomination are needed to dispense the requested amount. The program 
must ensure that the requested amount is valid (a multiple of 2, since there are no 
R$ 1 bills) and handle input errors if the user does not enter a valid numeric value.

Example input:
Enter the withdrawal amount: 188

Expected output:
Bills dispensed:
1 x R$ 100
1 x R$ 50
1 x R$ 20
1 x R$ 10
1 x R$ 5
1 x R$ 2

If an invalid withdrawal amount is entered (an odd number):
Error: The amount must be a multiple of 2. """

BILLS = [100, 50, 20, 10, 5, 2]


def bank():
    while True:
        withdrawal_amount = get_withdrawal_amount()

        if not verify_value(withdrawal_amount):
            print("Error: The amount must be a multiple of 2.")
            continue

        dispensed_bills = withdraw(withdrawal_amount)
        show_bills(dispensed_bills)
        break


def get_withdrawal_amount():
    while True:
        try:
            return int(input("Enter the withdrawal amount: "))

        except ValueError:
            print("Error: Please enter a valid numeric value.")


def verify_value(value):
    return value > 0 and value % 2 == 0


def withdraw(value):
    best_combination = None

    def find_combination(remaining, bill_index, combination):
        nonlocal best_combination

        if remaining == 0:
            if (
                best_combination is None
                or len(combination) < len(best_combination)
            ):
                best_combination = combination.copy()
            return

        if bill_index == len(BILLS):
            return

        bill = BILLS[bill_index]

        for quantity in range(remaining // bill + 1):
            for _ in range(quantity):
                combination.append(bill)

            find_combination(
                remaining - quantity * bill,
                bill_index + 1,
                combination
            )

            for _ in range(quantity):
                combination.pop()

    find_combination(value, 0, [])

    if best_combination is None:
        return None

    dispensed_bills = {}

    for bill in best_combination:
        dispensed_bills[bill] = dispensed_bills.get(bill, 0) + 1

    return dispensed_bills


def show_bills(dispensed_bills):
    print("\nBills dispensed:")

    for bill, quantity in dispensed_bills.items():
        print(f"{quantity} x R$ {bill}")


bank()