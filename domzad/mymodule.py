from cmath import sqrt
from re import A

#1
def arithmetic(a1:float,sym:str,a2:float)->any:
    """Lihtne kalkulaator
    + - liitmine, - - lahutamine, * - korrutamine, / - jagamine
    :param float a1: Esimene arv
    :param float a2: Teine arv
    :param str sym: Tehe
    :rtype: var Määramata tüüp
    """
    if sym in ["+","-","/","*"]:
        if sym=="/" and a2==0:
            vas="Div/0"
        else:
            vas = eval(str(a1)+sym+str(a2))
    else:
        vas = "Tundmatu tehe!"
    return vas
#2
def  is_year_leap(aasta:int)->bool:
    """
    Liigaasta leidmine
    Tagastab True kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype: bool Funktsioni vastus loogilises formaadis
    """
    aasta = int(aasta)
    if aasta%4==0:
        t=True
    else:
        t=False
    return t
#3
def square(a:float)->float:
    """Läbimõõdu, pindala ja diagonaali leidmine
    :param float number: Teie number
    :rtype:
    """
    try:
        a=float(a)
        if a>0:
            P = 4*a
            S = a**2
            d = a*sqrt(2)
            return P,S,d
        else:
            v="----"
            return v
    except:
        v="---"
        return v
   
#4
def season(num):
    """Вычислитель сезонов / времён года.

    """
    
   if num == 12 or 1 <= num <= 2:

       print("Talv")

   elif  3 <= num <= 5:

       print("Kevad")

   elif 6 <= num <= 8:

       print("Suvi")

   elif 9 <= num <= 11:

       print("Sügis")

   else:

       print("Valed andmed") 
#5
def bank(n, y):
    """Panga intressi kalkulaator
    """
    raha = n
    years = y
    def money():
        if years >0:
                raha = n*1.1
                years = years -1
                return money()
        else:
                return raha

        print(raha)
#6
def is_prime(n):
    """Вычислитель простого числа.
    
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(2)) 
print(is_prime(4))

#7
from datetime import datetime

def date(day, month, year):
    """Вычислитель дат в календаре.
    """
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

print(date(31, 12, 2022)) 
print(date(30, 2, 2022)) 
