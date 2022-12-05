from math import *
from random import *
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
a = int(input("Сколько газонокосилок?: "))
b = int(input("Сколько работали?: "))
m*=60
summa=0
for i in range(1,a):
    summa+=m
    m+=10
print("Всего они работают: ",summa/60)

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

#Задание 16
for r in range(9):
    for c in range(9):
        if r==c:
            print(r+1,end=" ")
        else:
            print(0,end=" ")
    print()

#Задание 10
for i in range(1,11):
    arv1 = randint(-100,100)
    arv2 = randint(-100,100)
    if arv1>arv2:
        print(f"{arv1} больше чем ",arv2)
        text+=" "+str(arv1)
    elif arv>arv1:
        print(f"{arv2} больше чем ",arv1)
        text+=" "+str(arv2)
    else:
        print(f"{arv1}, {arv2} равны ")
print(text)

#Таблица умножения
for r in range(1,11):
    for c in range(1,11):
        print(str(r+c).center(4),end=" ")
    print()

#Задача
r=0
c=0
while r<11:
    r+=1
    while c<11:
        c+=1
        print(str(r*c).center(4),end=" ")
    c=0
    print()#\n


