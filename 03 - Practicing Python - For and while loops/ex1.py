""" André is testing a new feature in the Buscante backend that processes data in a 
loop. During testing, he noticed that the system stopped responding and suspects the 
problem lies in an infinite loop. 

counter = 0

while counter < 10:
    print("Processing data...")"""

counter = 0

while counter < 10:
    print(f"Processing data...{counter}")
    counter += 1
