""" #Exercises

2 - Print the phrase: My name is {name} and I am {age} years old, where name and age must be values ​​stored in variables.
3 - Print the word ‘ALURA’ so that each letter appears on a separate line. 
4 - Print the phrase: The rounded value of pi is: {rounded pi}, where the value of pi must be stored in a variable and rounded to just two decimal places."""

# 1 - Print the phrase: Python at the Alura Programming School.
import math
print('Python at the Alura Programming School.')

# 2 print the phrase: My name is {name} and I am {age} years old, where name and age must be values ​​stored in variables.
name = 'John'
age = 30
print(f'My name is {name} and I am {age} years old.')

# 3 - Print the word ‘ALURA’ so that each letter appears on a separate line.
print('A\nL\nU\nR\nA')

# 4 - Print the phrase: The rounded value of pi is: {rounded pi}, where the value of pi must be stored in a variable and rounded to just two decimal places.
pi = math.pi
print(f'The rounded value of pi is: {pi:.2f}')
