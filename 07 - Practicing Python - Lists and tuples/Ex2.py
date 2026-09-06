""" A school held an essay competition, and the next step is to organize the
participants' scores to determine the award order. To ensure transparency,
the scores need to be sorted in ascending order, from the lowest to the highest value.

Based on this, develop a program that receives as input a list containing the
scores of all participants and displays, at the end, the list sorted in ascending order.

Input Example:

Scores: [85, 70, 90, 60, 75]

Expected Output:

Sorted scores: [60, 70, 75, 85, 90] """

scores = [85, 70, 90, 60, 75]
print(f'Notas originais: {scores}')
scores.sort()
print(f'Notas Organizadas: {scores}')
