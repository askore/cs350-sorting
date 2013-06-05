from random import *
of = open("10million.txt","a")
for i in range(0,10000000):
    rand = randint(1,10000000)
    of.write(str(rand) + "\n")

of.close()
