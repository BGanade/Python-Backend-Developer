""" "Mariana is responsible for granting access to the office and needs a program that
checks whether employees are allowed to enter. To do this, she will use the current 
time. The office only permits access between 8:00 AM and 6:00 PM. Create a program 
that takes the current time as input (in 24-hour format) and displays a message 
stating whether access is allowed or denied." """

hour = int(input("Enter the current hour (0-23): "))

if not 0 <= hour <= 23:
    print("Invalid hour.")
elif 8 <= hour <= 18:
    print("Access granted.")
else:
    print("Access denied.")
