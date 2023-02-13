from math import isqrt


def arithmetic(a1:float,symbol:str, a2:float)-> any:    
    if symbol in ['+','-','/','*']:
        
        if symbol=='/' and a2==0:
            answer='Div/0'
        else:
            answer=eval(str(a1)+symbol+str(a2))

    else:
        answer='Unknow action !'

    return answer

def is_year_leap(leap_year:int):

    leap_year=int(leap_year)

    if leap_year%4==0:

        answer1=True
    else:

        answer1=False

    return answer1

def square(a: float):

    try:
        a=float(a)
        if a>0:

            p=4*a
            s=a*a
            d=a*isqrt(2)
            return p,s,d
        else:
            v='---'
            return v
    except:
        v='---'
        return v



def season(month):
    if month in (1,2,12):
        return 'winter'
    elif month in (3,4,5):
        return 'spring'
    elif month in(6,7,8):
        return 'summer'
    elif month in(9,10,11):
        return 'autumn'
    else:
        return 'Error'





def bank(p,years):
    
   
    for each_year in range(years):
        p = (p * 1.1)
    return p




def is_prime(ordinary):
    
    for i in range(2, (ordinary//2)+1):
        if ordinary % i == 0:
            return False
    return True 



import datetime
def date(y:int,m:int,d:int):
    
    try:
        data=datetime.date(y,m,d)
        print(data)
        print("existing date")
    except:
        print("such date doesnt exist")

        return date
 



def xor_cipher(str,key):
    
    encript_str=""
    for letter in str:
        encript_str+=chr(ord(letter)^key)

    return 
