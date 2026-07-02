""" Fernanda is planning a trip and wants to calculate how much she will pay in tolls. 
The toll amount depends on the distance traveled:

Up to 100 km: R$ 10.00
Between 100 km and 200 km: R$ 20.00
Over 200 km: R$ 30.00
Create a program that takes the distance traveled as input and displays the 
corresponding toll amount. """

kilometers = int(input('Enter the distance you will travel (km): '))
if kilometers > 200:
    print('You will pay R$ 30.00 in tolls.')
elif kilometers > 100:
    print('You will pay R$ 20.00 in tolls.')
else:
    print('You will pay R$ 10.00 in tolls.')
