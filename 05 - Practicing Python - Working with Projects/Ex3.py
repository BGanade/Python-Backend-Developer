""" Mariana is a Portuguese language teacher and wants a program that counts how many 
vowels are in a text entered by her students. This will help analyze the structure of 
the words they use.

Create a program that asks the user to enter a text and displays how many vowels (a, e,
 i, o, u) it contains.

Example input:

Enter a text: The Python programming language is very versatile.

Expected output:

The text contains 13 vowels. """

text = input("Enter a text: ").lower()

def vowels_counter(text):
    vowels = "aeiou"
    vowel_count = sum(1 for char in text if char in vowels)
    return vowel_count

print(f"The text contains {vowels_counter(text)} vowels.")
