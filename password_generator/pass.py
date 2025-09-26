import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
symbols = string.punctuation
all_chars = uppercase + lowercase + digits + symbols
password = ""

pass_length = int(input("Password Length: "))

for i in range(pass_length):
    password += random.choice(all_chars)

print("Your password is: ", password)