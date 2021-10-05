import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '@#$%&*-_=+\/'

y_or_n = input("\nYou want a password with specials symbols? (y or n)\n")
if y_or_n == "y":
    characters = lower + upper + numbers + symbols
elif y_or_n == "n":
    characters = lower + upper + numbers
length = int(input("\nPut the password size here, enter with a value between 4 and 16:\n"))
password = "".join(random.sample(characters, length))
print("\n", password)