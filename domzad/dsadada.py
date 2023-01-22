from mymodule import *

#1
answer = arithmetic(2.5,"+",1.8)
print(answer)
answer = arithmetic(input(),input(),input())
print(answer)

#2
if is_year_leap(input()):
    print("Liidaasta")
else:
    print("Tavaline aasta")

#3
P,S,d = square(input())
print(f"Läbimõõt: {P}")
print(f"Pindala: {S}")
print(f"Diagonaal: {d}")

#4
n = int(input("Kirjutage oma aastaaega numbri (1-12): "))

season(n)

#5
n = int(input())
y = int(input())

#6
bk = int(input())

#7
kalen = int(input())