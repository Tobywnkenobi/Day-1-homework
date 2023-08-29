import math


"""
Get Prime numbers up to 100
 HINT::
 An else after an if runs if the if didnt
 An else after a for runs if the for didnt break

not divisible by any number other than itself

print(9%9)           n%n==0  n%1==0  n%(any other number)!=0
print(9%1)             So, prime % would equal 0, only if itself or 1..but we can skip one, but I'm not.
print(9%4)
no - going with the square root option..
"""
for num in range(2, 101):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)