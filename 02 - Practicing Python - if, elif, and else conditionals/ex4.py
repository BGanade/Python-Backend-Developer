""" Anna Júlia is creating a system to calculate Body Mass Index (BMI) and provide basic
 recommendations. The program must take a person's weight and height as input and 
 display the BMI value, as well as indicate whether the person is underweight, at a 
 normal weight, or overweight. Create a program that accepts weight (in kg) and height 
 (in meters) and calculates the BMI using the formula: BMI = weight / (height ** 2). 
 Then, display the BMI value and a message indicating whether the person is underweight 
 (BMI < 18.5), at a normal weight (18.5 <= BMI < 25), or overweight (BMI >= 25). """

weight = float(input('Please, Insert your weight in Kg: '))
height = float(input('Please, Insert your height in Meters: '))
BMI = weight/(height**2)
if BMI >= 25:
    print(f'Your BMI is {BMI}, you are overweight')
elif BMI >= 18.5:
    print(f'Your BMI is {BMI}, you are in normal weight')
else:
    print(f'Your BMI is {BMI}, you are underweight')
