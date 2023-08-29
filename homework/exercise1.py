"""
Cube Number Test... Print out all cubed numbers up to the total value 1000. 
Meaning that if the cubed number is over 1000 break the loop.
for loop.  (for every number=self*self*self) < 1000


"""
for n in range(1, 100):
    cube = n**n
    if cube <= 1000:
        print(cube)
    else:
        pass

print("that's all folks!")
