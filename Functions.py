from cmath import sqrt
from re import A


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
   

def season(num):

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
