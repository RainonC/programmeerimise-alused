from datetime import *
from Oma_moodul import *

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
                    vastus=Kontroll(ik)                    
                    if type(vastus)==int:
                        ik3 = int(ik_l[7:10])
                        haigla=Haigla(ik3)
                        print(haigla)
                        sugu=Sugu(int(ik_l[0]))
                        print(sugu)
                    else:
                        print(vastus)




                
            else:
                print("Esimene sümbol või arv on vale ") 
        except:
            print("Andmetüüp on vale, on vaja numbreid sisestada ")
    else:
        print("Sümbolite arv peab olema 11! ")