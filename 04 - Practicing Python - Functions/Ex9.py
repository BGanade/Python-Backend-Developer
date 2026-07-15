""" Miguel is developing a discount coupon system and needs a way to apply different 
discount rates to purchase amounts.

Based on this problem, create a closure that generates a function capable of calculating
 the final price with a fixed discount defined by the user.

Example input:
Enter the discount percentage: 10
Enter the purchase amount: 200

Expected output:
Final price with discount: 180.0 """

discount_percentage = int(input('Enter the discount percentage: '))
purchase_amount = int(input('Enter the purchase amount: '))

def price_calculator(discount, purchase):
    return purchase * (1 - discount/100)

print(f'final price with discount {price_calculator(discount_percentage, purchase_amount)}')