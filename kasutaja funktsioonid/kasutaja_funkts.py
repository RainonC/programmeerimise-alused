from module1 import *






answer=arithmetic(2.5, '+', 1.6)
print(answer)

while True:
    answer=arithmetic(input(),input(), input())
    print(answer)
    break



while True:

    if answer==is_year_leap(input('enter year:')):

        print('Leap year')
    else:
        print('ordinary year')
        break
    



p=square(input('Rectangle:'))
s=square(input('Area:'))
d=square(input('Dioganal:'))

print(f'Rectangle:{p}')
print(f'area:{s}')
print(f'diagonal:{d}')







while True:
    print(season(int(input('enter month:'))))

p=int(float(input("how a lot of money? ")))

years=int(float(input("how many years  for ? ")))

print(bank(p,years))



ordinary=int(input('enter a num:'))
print(is_prime(ordinary))




d=int(input("enter day"))
m=int(input("enter month"))
y=int(input("enter year"))

print(date(y,m,d))





strg=input('crypt:')
key=46
print('original:\t', strg )
encr_strg=xor_cipher(strg, key) 
print('encript:\t',encr_strg)
encr_strg=input('decryp:')
print('encript:\t',xor_cipher(encr_strg,key))
