""" Sara is participating in a writing competition, and one of the rules requires that 
each word in her text has a maximum character limit.

Help Sara by creating a function that takes a word as input and displays the number of 
characters it contains.

Example input:

Enter a word: technology

Expected output:

This word has 10 characters. """

word = input('Write something see how much characters ir countains: ')

def count_word_characters (word):
    return len(word)

word_length = count_word_characters(word)
print(f'the word "{word}" have {word_length} characters')