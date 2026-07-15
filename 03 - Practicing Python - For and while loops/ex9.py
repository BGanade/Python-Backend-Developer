""" João is developing a registration system for a reading website. He needs to ensure 
that users enter a valid username and password. The rules are as follows:

The username must have at least 5 characters.
The password must have at least 8 characters.
João wants the system to continue requesting the information until both conditions are 
met. When the user enters valid data, the program should display the message: 
"Registration completed successfully!".

Create a program that implements this logic using a while loop. """

while True:
    username = input("Enter a username with at least 5 characters: ")
    password = input("Enter a password with at least 8 characters: ")

    if len(username) >= 5 and len(password) >= 8:
        break

print("Registration completed successfully!")