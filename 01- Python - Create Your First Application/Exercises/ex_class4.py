""" 1 - Create a dictionary representing information about a person, such as name, age, and city.

2 - Using the dictionary created in step 1:

Modify the value of one of the items in the dictionary (for example, update the person's age);
Add a profession field for that person;
Remove an item from the dictionary.
3 - Create a dictionary that maps the numbers 1 through 5 to their respective squares.

4 - Create a dictionary and check if a specific key exists within it.

5 - Write code that counts the frequency of each word in a sentence using a dictionary. """

#1 --------------------------------------------------------------------------------------------------------------------
person = {'name': 'Bruno', 'age' : 29, 'city' : 'Elias Fausto'}
print(person)

#2 --------------------------------------------------------------------------------------------------------------------
#Updating age
person['age'] = 30

#updating profession
person['profession'] = 'engineer'

#removing a element
del person['city']

print(person)

#3 --------------------------------------------------------------------------------------------------------------------
square_number = {x: x**2 for x in range (1, 6)}
print(square_number)

#4 --------------------------------------------------------------------------------------------------------------------
person = {'name': 'Ganade', 'age': 19, 'city': 'São Luís'}
if 'name' in person:
    print("the key 'name' exist on the dictionarie")
else:
    print("the key 'name' doesnt exist. on the dictionarie")

#5 --------------------------------------------------------------------------------------------------------------------
sentence = "The quick brown fox jumps over the lazy dog. The brown dog was not amused."
words = sentence.lower().replace('.', '').split()
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency)