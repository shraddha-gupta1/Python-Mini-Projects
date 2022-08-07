import random

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghizklmnopqrstuvwxyz123456789!@#$"
length_password =int(input("Enter the length of the password: "))
a= "".join(random.sample(password,length_password))
print(f"Your password is:- {a} ") 