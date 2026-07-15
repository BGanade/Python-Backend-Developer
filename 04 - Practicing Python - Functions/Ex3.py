""" Beatriz is developing a customer service system for a service website. She wants to 
create a program that displays a personalized greeting based on the time of day the user
 accesses the platform. The system should follow these rules:

If the time is before 12:00, display "Good morning!";

Between 12:00 and 18:00, display "Good afternoon!";

After 18:00, display "Good evening!".

Example input:

Enter the current hour (0-23): 15

Expected output:

Good afternoon! """

time = int(input('Enter the current hour (0-23): '))

def hello_message(current_time):
    if current_time < 12:
        return 'Good morning!'
    elif current_time >= 18:
        return 'Good evening!'
    else:
        return 'Good afternoon!'
    
print(hello_message(time))
