from datetime import *

while True:
    ik = input("Isikukood: ")
    if len(ik)==11:
        try:
            ik_l = list(ik)
            if int(ik_l[0]) in [1,2,3,4,5,6]:
                if int(ik_l[0]) in [1,2]:
                    a=1800
                elif int(ik_l[0]) in [3,4]:
                    a=1900
                else:
                    a=2000
                aasta = 1900+int(ik_l[1]+ik_l[2])
                kuu = int(ik_l[3]+ik_l[4])
                paev = int(ik_l[5]+ik_l[6]) 
                if  datetime(aasta,kuu,paev):
                    pass
                
            else:
                print("Vale ") 
        except:
            print("Andmet��p on vale, on vaja numbreid sisestada ")
    else:
        print("S�mbolite arv peab olema 11! ")