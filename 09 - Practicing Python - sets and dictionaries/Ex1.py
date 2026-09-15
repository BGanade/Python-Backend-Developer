""" Ana is organizing a birthday party and needs a guest list that has no duplicates,
as some people were accidentally invited more than once. She would like the program
to ask for the guests' names and, at the end, display the organized list without 
duplicates.

Write a program that receives the guests' names until the user enters 'exit', and at
the end displays the guest list without duplicates.

Input Example:
Enter the guest's name: Ana
Enter the guest's name: João
Enter the guest's name: Ana
Enter the guest's name: Carla
Enter the guest's name: exit

Expected Output:
Confirmed guests: Ana, João, Carla """

guests = set()
while True:
    name = input("Enter the guest's name or exit to end: ")
    if name != 'exit' and name not in guests:
        guests.add(name)
    elif name in guests:
        print(f'The name {name} is already in the guest list')
    elif name.lower() == 'exit':
        break
confirmed_guests = ', '.join(sorted(guests))
print(f'Confirmed Guests: {confirmed_guests}')