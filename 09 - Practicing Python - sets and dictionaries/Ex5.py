""" Joana is a project manager and needs to consolidate the task lists of two
different teams. After combining the lists, she wants to remove a specific
task provided by the user. Your task is to create a program that performs
this operation.

Input Example:

team_a = {"plan meeting", "review document", "test system"}

team_b = {"test system", "implement feature", "fix bug"}

Expected Output:

Final tasks: {'implement feature', 'plan meeting', 'review document', 'fix bug'} """

team_a = {"plan meeting", "review document", "test system"}

team_b = {"test system", "implement feature", "fix bug"}

combined_tasks = team_a.union(team_b)

remove_task = input("Enter the task you want to delete: ").lower()

if remove_task in combined_tasks:
    combined_tasks.remove(remove_task)

print(f'Final tasks: {combined_tasks}')
