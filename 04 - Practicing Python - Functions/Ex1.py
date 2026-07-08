""" Julia is a teacher and needs a program to help her students calculate their ages 
based on their birth year. Your task is to create a function that takes the birth year 
and the current year as parameters and returns the corresponding age.

Example input:
Enter the birth year: 2005
Enter the current year: 2025

Expected output:
The age is 20 years. """

birth_year = int(input("Enter the year you were born: "))
current_year = int(input("Enter the current year: "))

def calculate_age(birth_year, current_year):
    return current_year - birth_year

age = calculate_age(birth_year, current_year)

print(f"The age is {age} years.")