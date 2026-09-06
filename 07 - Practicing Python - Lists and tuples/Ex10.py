""" A school is organizing student data to create a summary report. Each student has
their data recorded in a single entry, including their name, age, and final grade
for the semester. This data should be displayed separately for each student in
the following format:

Student: Name
Age: Age
Grade: Grade

Help the school develop a program that records the students' information, organizes
the data, and displays a detailed report with the information separately.

Input Example:

Enter the student data in the format Name, Age, Grade separated by commas:
João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8

Expected Output:

Student: João
Age: 16
Grade: 8.5

Student: Maria
Age: 17
Grade: 9.2

Student: Pedro
Age: 15
Grade: 7.8 """

data = input("Enter the student data in the format Name, Age, Grade separated by "
             "commas: ").split(", ")

for i in range(0, len(data), 3):
    name, age, grade = data[i], int(data[i + 1]), float(data[i + 2])
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}\n")
