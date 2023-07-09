#password generator

import random
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJLMNOPQRSTUVWXYZ1234567890''!@#$%^&*"
n=int(input("length of password"))
password= " "

for i in range(n):
    password += random.choice(char)
print(password)
