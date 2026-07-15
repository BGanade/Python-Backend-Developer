""" Pedro is creating a product registration system for his store and noticed that all 
of his customers' phone numbers are stored as strings. However, to make searching and 
validation easier, he needs these phone numbers to be treated as integers.

Given the following code with a list of phone numbers incorrectly stored as strings, 
create two functions: one that converts the values to integers, and another that 
verifies whether the conversion was successful and confirms that all phone numbers are 
integers.

Example input:

phone_numbers = ["11987654321", "21912345678", "31987654321", "11911223344"]

Expected output:

All phone numbers were converted successfully! """

phone_numbers = ["11987654321", "21912345678", "31987654321", "11911223344"]

def convert_items(numbers):
    return [int(number) for number in numbers]

def verify_conversion(numbers):
    return all(type(number) == int for number in numbers)

phone_numbers = convert_items(phone_numbers)

if verify_conversion(phone_numbers):
    print("All phone numbers were converted successfully!")
else:
    print("Some phone numbers were not converted.")
