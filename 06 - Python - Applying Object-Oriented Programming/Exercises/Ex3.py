""" In Python, creating classes is an essential part of object-oriented programming. 
Below, we have an example of a class called Music that represents information about a 
song, such as its name, artist, and duration:

class Music:
    name = ''
    artist = ''
    duration = int

Now it's your turn! Rewrite this Music class using a more concise and expressive 
approach, taking advantage of Python's simplified syntax. """ 

class Music:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

music1 = Music('Never the less', 'Phaxe', '6:40')
music2 = Music('Gods Dont Pray', 'Imagine Dragons', '2:50')
music3 = Music('Fina Ironia Divina', 'Matanza Inc', '3:38')

print(vars(music1))
print(vars(music2))
print(vars(music3))