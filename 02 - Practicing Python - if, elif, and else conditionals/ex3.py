""" Lucas works in IT and needs to ensure that the temperature of a server room
does not exceed 25°C. He wants a program that takes the current temperature as input 
and, if necessary, displays an alert message. """

server_temperature = float(input('Enter the current server temperature:'))

if server_temperature > 25:
    print(f"""Alert! The server temperature is {server_temperature}°C, which exceeds the
           safe limit.""")
else:
    print(f'The server temperature is ok, current temperature {server_temperature}°C')
