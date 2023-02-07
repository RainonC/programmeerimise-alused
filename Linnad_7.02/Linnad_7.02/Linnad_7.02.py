#Rainon Kaska TARgv22
#Все что было отмечено # в коде- это попытки написания, более подходящего к заданию, кода. Пытался сделать запись в
#отдельные файлы, но постоянно выдавало ошибку, как бы не исправлял код.
#В итоге получилось так, чтобы все данные не записывались в отдельные txt файлы. :(

from mymodule import *
linnad = []
kodanikud = []

while True:
    linn = input("Sisestage linn: ")
    kodanikud1 = int(input("Sisestage linna kodanikku arv: "))
    linnad.append(linn)
    kodanikud.append(kodanikud1)
    lahk = input("Sisestage 'q' kui tahate lahkuda lisamisest \
või Enter jätkamiseks: ")
    if lahk.lower() == 'q':
        break

#while True:
#    v=int(input("0-loe failist \n1-andmete lisamine \n2-salvestamine failisse\n"))
#    if v==0:
#        linnad=[]
#        kodanikud=[]
#        linnad=loe_failist("linnade_fail.txt")
#        kodanikud=loe_failist("inimesed_fail.txt")
#        print(linnad)
#        print(kodanikud)
#    elif v==1:
#        linnad, kodanikud=elem_listisse(linnad,kodanikud)
#        print(linnad)
#        print(kodanikud)
#    elif v==2:
#        list_failisse(linnad,"linnade_fail.txt")
#        list_failisse(kodanikud,"inimesed_fail.txt")
#    lahk = input("Sisestage 'q' kui tahate lahkuda lisamisest \
#või Enter jätkamiseks: ")
#    if lahk.lower() == 'q':
#        break

##while True:
##    linnad, kodanikud = elem_listisse(linnad,kodanikud)
##    print(linnad)
##    print(kodanikud)
##    lahk = input("Sisestage 'q' kui tahate lahkuda lisamisest \
###või Enter jätkamiseks: ")
##    if lahk.lower() == 'q':
##        break

linn_dict = dict(zip(linnad, kodanikud))



while True:
    command = input('Valik: 1- sisestanud linna järgi, näitab kodanikke arv\n2- Kuva tähestikulises järjekorras linnade nimekiri ja elanike arv\n3- Leidke kõige suurema rahvaarvuga linn\n4- Leidke linnad, kus on vähem kui n elanikku\nq- lahkumiseks ')
    if command == '1':
        linn = input('Sisestage linn: ')
        print(populatsioon(linn, linn_dict))
    if command == '2':
        print(show_inf(linn_dict))
    if command == '3':
        print(most_pop(linn_dict))
    if command == '4':
        num = int(input('Sisestage kodanikke arv: '))
        print(less(linn_dict, num))
    if command == 'q':
        break