""" "Mariana is responsible for granting access to the office and needs a program that
checks whether employees are allowed to enter. To do this, she will use the current 
time. The office only permits access between 8:00 AM and 6:00 PM. Create a program 
that takes the current time as input (in 24-hour format) and displays a message 
stating whether access is allowed or denied." """

hour = int(input('enter the current time: '))
if hour >= 8 and hour <= 18:
    print('You can enter the office!!')
else:
    print('You cant enter the office!!')
