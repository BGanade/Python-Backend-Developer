""" In object-oriented programming (OOP), a class is a blueprint for creating objects. 
An object is a specific instance of a class, and classes are used to define the behavior
 and properties shared by a group of related objects.

For example, a Music class could have 3 attributes that represent the characteristics or
 properties of an object:

name
artist
duration

Now it's your turn! Create a class called Music with the following attributes and create
 3 objects, defining each attribute. """

class Music:
    name = '' 
    artist = ''
    duration = ''

music1 = Music()
music2 = Music()
music3 = Music()
music1.artist = 'Phaxe'
music1.duration = '6:40'
music1.name = 'Never the less'
music2.artist = 'Imagine Dragons'
music2.duration = '2:50'
music2.name = 'Gods Dont Pray'
music3.artist = 'Matanza Inc'
music3.duration = '3:38'
music3.name = 'Fina Ironia Divina'

print(vars(music1))
print(vars(music2))
print(vars(music3))