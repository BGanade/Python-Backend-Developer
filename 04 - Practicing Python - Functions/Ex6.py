""" Lucas is developing a system to generate financial reports and needs to filter only 
the even numbers from a list provided by the user.

Create a program that reads a list of numbers and displays only the even ones using the 
filter() function.

Example input:

Enter the numbers separated by spaces: 1 2 3 4 5 6

Expected output:

Even numbers: 2 4 6 """

numbers = input("Enter numbers separated by spaces: ").split() 
even = filter(lambda x: int(x) % 2 == 0, numbers) 
print("Even numbers:", " ".join(even))