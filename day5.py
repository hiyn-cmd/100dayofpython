import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_char = nr_numbers + nr_symbols + nr_letters

alllet = []
allsym = []
allnum = []

for let in range(1,nr_letters + 1):
    alllet += random.choice(letters)
for sym in range(1, nr_symbols + 1):
    allsym += random.choice(symbols)
for num in range(1, nr_numbers + 1):
    allnum += random.choice(numbers)

password_chars = alllet + allsym + allnum
password = ""

for char in range(1, nr_char + 1):
    password += random.choice(password_chars)

print(password)






