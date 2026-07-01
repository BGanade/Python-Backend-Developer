""" Bruno manages a small business and wants to know which product had the best sales 
performance last month. 
He recorded the sales quantities for two products: apples and bananas. Now, he needs to 
write a program 
that identifies and displays which one sold the most.

Create a program that takes the sales figures for the two products as input and displays
 a message indicating
 which one sold more. If the quantities are equal, display a message stating that there
   was a tie. """

apple_sales = int(input("Enter the quantity of apples sold last month: "))
banana_sales = int(input("Enter the quantity of bananas sold last month: "))

if apple_sales > banana_sales:
    print("Apples were the best-selling product last month.")
elif banana_sales > apple_sales:
    print("Bananas were the best-selling product last month.")
else:
    print("There was a tie in sales last month.")
