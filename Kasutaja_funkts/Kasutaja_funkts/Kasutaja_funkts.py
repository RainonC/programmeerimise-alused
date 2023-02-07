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
square=0
P,S,d = square(input())
print(f"Läbimõõt: {P}")
print(f"Pindala: {S}")
print(f"Diagonaal: {d}")

#4
month = input("Введите месяц (номер): ")
result = season(month)
print(f'Сезон для вашего месяца {month} это {result}')

#5
a = input("Введите депозит: ")
years = input("Введите срок: ")
final_amount = bank(a, years)
print(f'Через {years} лет, итоговая сумма будет {final_amount} EUR.')
#6
print(is_prime(input("Введите число: ")))
#7
print(date_exists(input("Введите число месяц год")))
