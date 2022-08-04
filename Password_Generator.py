# Edited password length

import random

password = ''
while True:
    password_length = int(input("Please enter length of password: (1-49)"))
    if 0 < password_length <50:
        break
for i in range(10):
    random_integer = random.randint(33,126)
    password += chr(random_integer)
print("Password: ", password)

