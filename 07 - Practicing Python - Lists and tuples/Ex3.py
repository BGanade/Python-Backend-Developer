""" An NGO is organizing a food donation campaign and needs to register the names
of the volunteers who will help with the event. As volunteers sign up, their names
should be added to the list, and when the word 'exit' is entered, the program should 
end.

Help the NGO create a program that allows volunteers to be registered and displays
the complete list at the end.

Input Example:

Enter the volunteer's name (or 'exit' to finish): Ana
Enter the volunteer's name (or 'exit' to finish): John
Enter the volunteer's name (or 'exit' to finish): Mariana
Enter the volunteer's name (or 'exit' to finish): exit

Expected Output:

Registered volunteers: ['Ana', 'John', 'Mariana'] """

volunteers = []

while True:
    volunteer = input('Enter the volunteers name or "exit" to finish: ')
    if volunteer.lower() == "exit":
        break
    else:
        volunteers.append(volunteer)

print(f'Registered volunteers: {volunteers}')
