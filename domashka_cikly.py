from math import *
#Задание 1
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

#Задание 12
a= int(input("Сколько газонокосилок?: "))
b=int (input("Сколько работали?: "))
b_1=b*60
for i in range(1,a):
    c1=i*b_1
    a1=b*70
    print(c1+a1)

#Задание 7
k = int(input('k = '))
a = int(input('a = '))
b = int(input('b = '))
c = int(b+1)


for i in range(a,c):
    l = i/k
    print(l)

#Задание 2
a = int(input('a = '))
c = int(a + 1)
sum = 0
for i in range(1, c):
    sum+=i
print(sum)

#Задание 17
n = int(input('Введите n: '))
for i in range(1, 11):
    print(f'{n} * {i} = {n*i}')

#Задание 20
num = 0

sum = 0

for i in range(1,51):
    if i % 5 == 0 or i % 7 == 0:
        print(i)

#Задание 22
sum = 0
for i in range(100,200):
    if i % 17 == 0:
        sum+=i
        print(sum)

#Задание 9
n = int(input("Депозит: "))
s = int(input("Количество лет: ")) 
z = 0
for i in range(s*12):
    z = n*0.03/12
    n+=z
    output=n
print(n)