""" João works as a waiter at a restaurant and needs to calculate the tip that customers
 leave when paying their bill. The restaurant suggests a 10% tip, but some customers may
   choose to give more or less.

To speed up the process, João wants a program that receives the total bill amount and 
the desired tip percentage, then displays the final amount the customer should pay.

Create a program that asks the user for the bill amount and the tip percentage. The 
program should calculate and display the tip amount and the total amount to be paid.

Example input:

Enter the bill amount: 120.00
Enter the tip percentage: 10

Expected output:

Tip amount: $12.00
Total to pay: $132.00 """

bill_amount = float(input('Enter the bill amount $: '))
tip_percentage = float(input('Enter the tip percentage %: '))


def tip_calculator(tip_percentage):
    def calculate_total(bill_amount):
        tip_amount = bill_amount * tip_percentage / 100
        return bill_amount + tip_amount

    return calculate_total


calculate_bill = tip_calculator(tip_percentage)

total = calculate_bill(bill_amount)

tip_amount = bill_amount * tip_percentage / 100

print(f'Tip amount: ${tip_amount:.2f}')
print(f'Total to pay: ${total:.2f}')