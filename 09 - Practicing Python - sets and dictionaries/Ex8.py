""" Lucas is a volunteer helping organize a marathon and received a list of
participants along with their respective ages. Now, he needs a program that
displays three pieces of information:

- The names of all participants.
- The ages of all participants.
- A complete list with each participant's name and age.

Your task is to create this program based on the provided information.

Input Example:

participants = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
}

Expected Output:
Participant names: Mariana, Carlos, Beatriz, Rafael
Participant ages: 25, 32, 28, 35
Participants and their ages:
- Mariana: 25 years old
- Carlos: 32 years old
- Beatriz: 28 years old
- Rafael: 35 years old """

participants = {
    "Mariana": 25,
    "Carlos": 32,
    "Beatriz": 28,
    "Rafael": 35
}

print(f"Participant names: {', '.join(participants.keys())}")
print(
    f"Participant ages: {', '.join(str(age) for age in participants.values())}"
)

print("Participants and their ages:")

for name, age in participants.items():
    print(f"- {name}: {age} years old")
