""" A teacher needs a program that helps calculate students' final averages and 
indicates whether they passed, need to take a remedial exam, or failed. The rules are:

Average >= 7: Passed
5 <= Average < 7: Remedial Exam
Average < 5: Failed
Write a program that takes three grades as input and calculates the final average. 
Based on the average, display the student's status. """

first_exam = float(input('Enter the first exam grade: '))
second_exam = float(input('Enter the second exam grade: '))
third_exam = float(input('Enter the third exam grade: '))

average = (first_exam + second_exam + third_exam) / 3

if average >= 7:
    print(f'You passed with an average of {average:.2f}.')
elif average >= 5:
    print(f'Your average is {average:.2f}. You need to take the remedial exam.')
else:
    print(f'You failed with an average of {average:.2f}.')

