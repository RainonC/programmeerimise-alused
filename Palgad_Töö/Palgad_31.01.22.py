from omamoodul import *
palgad=[]
nimed=[]

palgad=loe_failist("palgade_fail.txt")
print(palgad)
nimed=loe_failist("nimede_fail.txt")
print(nimed)



while True:
    v=int(input("0-loe failist \n1-andmete lisamine \n2-salvestamine failisse\n3-kustuta nimi failist\n4-maksimaalne palk\n5-minimaalne palk\nValik: "))
    if v==0:
        palgad=[]
        nimed=[]
        palgad=loe_failist("palgade_fail.txt")
        nimed=loe_failist("nimede_fail.txt")
        print(palgad)
        print(nimed)
    elif v==1:
        palgad, nimed=elem_listisse(palgad,nimed)
        print(palgad)
        print(nimed)
    elif v==2:
        list_failisse(palgad,"palgade_fail.txt")
        list_failisse(nimed,"nimede_fail.txt")
    elif v==3:
        palgad,nimed=kustutamine(input("Sisesta nimi: "), palgad,nimed)
        print(palgad)
        print(nimed)
    elif v==4:
        maksimaalne_palk(palgad,nimed)
    elif v==5:
        minimaalne_palk(palgad,nimed)