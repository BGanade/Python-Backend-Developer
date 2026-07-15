""" Paulo is developing a program to calculate accumulated values in a financial system.
 He needs to add all the integers from 1 to n, where n is a value chosen by the user.

Help Paulo by creating a recursive function that receives a number n and returns the sum
 of all integers from 1 to N.

Example input:
Enter a number: 5

Expected output:
The sum from 1 to 5 is: 15 """

sum_limit_number = int(input("Enter a number: "))


def recursive_sum(number):
    if number == 1:
        return 1

    return number + recursive_sum(number - 1)


print(f"The sum from 1 to {sum_limit_number} is: {recursive_sum(sum_limit_number)}")