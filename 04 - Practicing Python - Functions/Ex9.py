""" Miguel is developing a discount coupon system and needs a way to apply different 
discount rates to purchase amounts.

Based on this problem, create a closure that generates a function capable of calculating
 the final price with a fixed discount defined by the user.

Example input:
Enter the discount percentage: 10
Enter the purchase amount: 200

Expected output:
Final price with discount: 180.0 """

discount_percentage = int(input("Enter the discount percentage: "))
purchase_amount = float(input("Enter the purchase amount: "))


def create_discount_calculator(discount):
    def calculate_price(purchase):
        return purchase * (1 - discount / 100)

    return calculate_price


discount_calculator_10 = create_discount_calculator(discount_percentage)

final_price = discount_calculator_10(purchase_amount)

print(f"Final price with discount: {final_price}")