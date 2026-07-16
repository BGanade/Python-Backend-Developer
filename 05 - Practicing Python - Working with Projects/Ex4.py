""" Sofia is a proofreader and needs to identify very long words in a paragraph. Texts 
are usually easier to read when they contain shorter words, so she wants a program that 
finds and displays all words with more than 10 letters.

Create a program that reads a text and displays all words that contain more than 10 
letters. If no long words are found, the program should notify the user.

Example input:
Enter a text: Structured programming made the development of large computer systems 
easier.

Expected output:
Long words found: programming, structured, development, computer, systems

If no long words are found:
No long words were found in the text. """

text = input('Enter a text: ').split()


def find_long_words(text):
    long_words = []

    for word in text:
        if len(word) > 10:
            long_words.append(word)

    if not long_words:
        return 'No long words were found in the text.'

    return f'Long words found: {", ".join(long_words)}'


print(find_long_words(text))