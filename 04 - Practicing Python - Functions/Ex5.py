""" Carlos works at a retail store and needs to calculate the total value of the day's 
sales. The sales amounts are entered on a single line, separated by spaces.

Your task is to create a program that reads this line, converts the values to numbers, 
and displays the total.

Example input:

Enter the sales amounts: 100 250 300

Expected output:

The total sales amount is: 650 """

values = input('Enter the sales values: ').split()
total = sum(map(float, values))
print(f'The total of sales was: {total:.0f}')