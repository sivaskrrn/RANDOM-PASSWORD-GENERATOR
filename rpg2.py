import random
import string 

length = int(input("enter the length of password:"))

letters = input("Include letters?(yes/no):").lower()
numbers = input("Include numbers?(yes/no):").lower()
symbols = input("Include symbols?(yes/no):").lower()
                
character=" "

if letters == "yes":
    character+=string.ascii_letters

if numbers=="yes":
   character+=string.digits

if symbols == "yes":
    character+=string.punctuation

password = ''.join(random.choice(character) for _ in range(length))

print("Generated Password:",password)