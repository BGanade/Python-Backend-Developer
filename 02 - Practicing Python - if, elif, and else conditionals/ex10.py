""" Pedro wants to apply for a loan, but approval depends on two conditions:

His monthly income must be greater than R$ 2,000.00.
The installment amount cannot exceed 30% of his income.
Create a program that takes Pedro's monthly income and the desired installment amount 
as input. The program must indicate whether the loan is approved or denied based on the 
conditions above. """

income = float(input('Enter your monthly income: '))
installment_amount = float(input('Enter the installment amount: '))

if income > 2000 and installment_amount <= income * 0.3:
    print('Loan approved!')
else:
    print('Loan denied!')