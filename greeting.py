name = input ("What is your name? ")
print (f"Hello, {name}!")

Age = input ("How old are you? ")
if Age.isdigit() and int(Age) >= 18:
    print (f"You are {Age} years old!")
elif int(Age) < 18:
    print (f"You are {Age} years old! You are not allowed to enter this site.")

else:
    Age = input ("How old are you? ")
if Age.isdigit() and int(Age) >= 18:
    print (f"Welcome to python!")
