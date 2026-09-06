""" The Alura Runners athletics club organized a race and published the final
ranking of the participants. However, an error was identified: one of the names
is incorrect. The organizer needs a program that allows them to find the wrong
name and replace it with the correct one.

How would you write a program that asks for the wrong name, the correct name,
and updates the list by displaying the new ranking at the end?

Input Example:

Enter the incorrect name: Carlos
Enter the correct name: João

Expected Output:

The name Carlos was replaced by João.
Updated ranking: ['Ana', 'João', 'Pedro'] """

ranking = ['Ana', 'Carlos', 'Pedro']

incorrect_name = input('Enter the incorrect name: ')

if incorrect_name in ranking:
    correct_name = input('Enter the correct name: ')

    position = ranking.index(incorrect_name)
    ranking[position] = correct_name

    print(f'The name {incorrect_name} was replaced by {correct_name}.')
    print(f'Updated ranking: {ranking}')
else:
    print('Name not found.')
