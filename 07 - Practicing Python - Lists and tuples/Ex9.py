""" Professor Helena wants to make her routine easier when calculating the average
of the final grades for her class. She always records the students' grades
throughout the semester, and at the end, she needs a report to see how well
the class is doing.

To help her, create a program that receives the final grades of all students
and calculates the class average.

Input Example:

Enter the students' grades separated by commas: 8.5, 7.0, 9.2, 6.8

Expected Output:

Final class average: 7.88 """

grades = input('Enter the students grades separated by commas: ').split(', ')
grades = [float(grade) for grade in grades]
print(grades)
average = sum(grades) / len(grades)
print(f'final class average: {average:.2f}')
