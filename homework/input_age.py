"""
Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age range:
age<18 - print kids                 18<age<65 - print adults    age>65 - print seniors

if loop.  if else.  after the input.
"""
age = int(input("What is your age?"))

if age < 18:
    print(str(age) + " You are a mere child!")
elif 18 <= age <= 65:
    print(str(age) + " Act like an adult!!")
elif age > 65:
    print(str(age) + " Winter is Coming")