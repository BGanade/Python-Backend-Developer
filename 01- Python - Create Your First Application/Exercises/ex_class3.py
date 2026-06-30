""" 1 - Create a list for each of the following items:

A list of numbers from 1 to 10;
A list containing four names;
A list containing your birth year and the current year.

2 - Create a list and use a `for` loop to iterate through all the elements of the list.

3 - Use a `for` loop to calculate the sum of odd numbers from 1 to 10.

4 - Use a `for` loop to print the numbers from 1 to 10 in descending order.

5 - Ask the user for a number and then use a `for` loop to print the multiplication table for that number, from 1 to 10.

6 - Create a list of numbers and use a `for` loop to calculate the sum of all elements. Use a `try-except` block to handle potential exceptions.

7 - Write code to calculate the average of the values in a list. Use a `try-except` block to handle division by zero in case the list is empty. """

#1 --------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-1 ----------')
numbers = list(range(1, 11))
names = ['Alice', 'Bob', 'Charlie', 'David']
years = [1990, 2023]


#2 --------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-2 ----------')
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

#3 --------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-3 ----------')
odd_sum = 0
for num in range(1, 11):
    if num % 2 != 0:
        odd_sum += num
print(f"The sum of odd numbers from 1 to 10 is: {odd_sum}")

#4 --------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-4 ----------')
for num in range(10,0,-1):
    print(num)  

#5 --------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-5 ----------')
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#6 --------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-6 ----------')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
sum_numbers = 0

for number in numbers:
    sum_numbers += number

print(f'The sum of the numbers is {sum_numbers}')

#7---------------------------------------------------------------------------------------------------------------------------------------------------
print('ex-7 ----------')
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_list = 0

for number in num_list:
    sum_list += number

try:
    average = sum_list / len(num_list)
    print(f'The average is {average}')

except ZeroDivisionError:
    print('The list is empty.')