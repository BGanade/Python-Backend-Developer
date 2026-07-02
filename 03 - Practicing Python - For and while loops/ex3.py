""" You are receiving a list of values ​representing your online store's products and 
would like to calculate the total sum of these products to understand the weekly 
financial performance. 

values = [10, 20, 30, 40, 50]
"""

values = [10, 20, 30, 40, 50]
sum_sells = 0

for value in values:
    sum_sells += value
print(f'The amount selled is {sum_sells}')
