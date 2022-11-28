from math import *
i=0
j=0
for i in range(0,15,1): #for i in range(15)
    A = float(input(f"{i+1} Sisesta A: "))
    if int(A) == A: j+=1
print(j)

i=0
j=0
while i<15:
    i+=1
    A = float(input(f"{i} Sisesta A: "))
    if int(A) == A: j+=1
print(j)

