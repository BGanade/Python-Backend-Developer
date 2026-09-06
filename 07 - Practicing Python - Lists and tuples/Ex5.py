""" Camila loves hosting friends for themed dinners. For the next gathering, she wants
to make sure the order of arrival is respected, but she still needs to make some
adjustments to the guest list. Camila wants to add new names and organize them
into specific positions.

How would you create a program that displays the initial list, allows the insertion
of a new name at a chosen position, and displays the updated list?

Input Example:

Current guest list: ['Ana', 'Pedro', 'Carlos']
Enter the name of the new guest: João
Enter the position where you want to insert the guest: 2

Expected Output:

Updated guest list: ['Ana', 'João', 'Pedro', 'Carlos'] """

guest_list = ['Ana', 'Pedro', 'Carlos']
print(f'Current guest list: {guest_list}')
new_guest = input('Enter the name of the new guest: ')
position_new_guest = int(
    input("Enter the position you want to insert the guest: "))
guest_list.insert(position_new_guest - 1, new_guest)
print(guest_list)
