#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ''
for each in range(1,nr_letters+1):
  password += random.choice(letters)
for each in range(1,nr_symbols+1):
  password += random.choice(symbols)
for each in range(1,nr_numbers+1):
  password += random.choice(numbers)

password_chars = list(password)
random.shuffle(password_chars)
password = ''.join(password_chars)
print(f"Your secure password is: {password}")


# safer_password_chars = []
# for i in range(1,len(password_chars)+1):
#   new = random.choice(password_chars)
#   password_chars.remove(new)
#   safer_password_chars.append(new)
# safer_password = ''.join(safer_password_chars)
# print(safer_password)