""" Laura is organizing a technology workshop and needs a program that allows her
to remove participants who have dropped out of the event. The system stores
participants in a dictionary, where each key is the workshop name and the value
is a set containing the participant data. The program should ask for a
participant's name and remove that name from the list of registered participants,
if it exists.

Input Example:
participants = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
}

Participant name to remove: Carla

Expected Output:
Updated participant list:
Workshop 1: {'Alice', 'Bruno', 'Diego'}
Workshop 2: {'Fernanda', 'Gustavo', 'Helena'} """

participants = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"}
}

participant_remove_name = input("Participant name to remove: ")

for workshop, names in participants.items():
    names.discard(participant_remove_name)

print('Updated list of participants: ')

for workshop, names in participants.items():
    print(f"{workshop}: {names}")
