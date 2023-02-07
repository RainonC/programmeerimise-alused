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
def season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"
    else:
        return "Ошибка!"
#5
def bank(a, years):
    for i in range(years):
        a += a*0.1
    return a

#6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True


#7
from datetime import date

def date_exists(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False
