from math import *
print("Tere olen sinu uus sõber - Python!")
name = input("Mis on sinu nimi?: ")
print(name + "," + "oi kui ilus nimi!")
ves = input(name + "!" + "Kas leian sinu keha indeksi? 0-ei, 1-jah => ")
if ves == "1":

    while True:

        try:
            pikkus = int(input("Mis on sinu pikkus?: "))
            if pikkus>0 and pikkus<273: break
        except:
            #pikkus = 175
            print("Error")
    mass=-1
    while mass<0 or mass>400:
        try:
            mass = int(input("Kui palju sa kaalud?: "))
        except:
            #mass = 68
            print("Error")
    try:
        indeks = mass/(0.01 * pikkus)**2
        if indeks<16:
            print("Tervisele ohtlik alakaal!")
        elif indeks>=16 and indeks<19:
            print("Alakaal")
        elif indeks>=19 and indeks<25:
            print("Normaalkaal")
        elif indeks>=25 and indeks<30:
            print("Ülekaal")
        elif indeks>=30 and indeks<35:
            print("Rasvumine")
        elif indeks>=35 and indeks<40:
            print("Tugev rasvumine")
        elif indeks>=40:
            print("Tervisele ohtlik rasvumine!")
    except:
        print("Error")


    
    


else:
    print("Kahju! See on väga kasulik info!")

print("Kohtumiseni, " + name + "! Igavesti Sinu, Python!")
