""" Clara is an editor for a magazine and wants to compare two articles to identify
which words appear in both. Your task is to create a program that receives two
texts and displays the set of words they have in common.

Input Example:

Text 1: The sun shines brightly in the blue sky

Text 2: The blue sky announces a sunny day

Expected Output:

Common words: {'the', 'blue', 'sky', 'sun'} """

text1 = set(input("Enter the first text: ").lower().split(' '))
text2 = set(input("Enter the second text: ").lower().split(' '))

common = text1.intersection(text2)

print(f'the common words between the first and second text are {common}')
