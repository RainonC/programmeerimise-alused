def loe_failist(file:str)->list:
    """Loeme failist read ja lisame järjendisse 
    :param str file: Faili nimetus
    """
    fail=open(file,'r',encoding="utf-8-sig")
    mas=[]
    for rida in fail:
        if rida.isdigit():
            mas.append(int(rida).strip())
        else:
            mas.append(rida.strip())
    fail.close()
    return mas

def list_failisse(mas:list,file:str):
    """Salvestamine loetelu failisse
    :param str file: Faili nimetus
    :param str mas: Loetelu
    """
    f=open(file,'w',encoding="utf-8-sig")
    for item in mas:
        f.write(item+"\n")
    f.close()

def elem_listisse(p:list,i:list):
    """
    """
    n=int(input("Mitu inimesi lisame? "))
    for j in range(n):
            nimi=input("Nimi: ")
            i.append(nimi)
            p=input("Palk: ")
            p.append(p)
    print(p)
    print(i)
    return p,i

def kustutamine(nimi:str,p:list,i:list):
    """Kustutame failist nime ja palga
    """
    n=i.count(nimi)
    pos=0
    for j in range(n):
        ind=i.index(nimi,pos)
        pos=ind
        i.remove(nimi)
        p.pop(ind)
    return p,i

#def str_to_int(mas:list)->list:
#    for m in mas:
#        ind=mas.index(m)
#        m=mas.pop(ind)
#        m=int(m)
#        mas.insert(m,ind)

def maksimaalne_palk(p:list,i:list):
    """Näitab maksimaalse palga listis
    """   
    p=list(map(int,p))
    max_palk=max(p)
    n=p.count(max_palk)
    pos=0
    print(f"Maksimaalne palk on {max_palk}\nInimeste nimed: ")
    for j in range(n):
        ind=p.index(max_palk)
        nimi=i[ind]    
        print(f"{nimi}")
        pos=ind+1

def minimaalne_palk(p:list,i:list):
    """Näitab minimaalse palga listis
    """
    p=list(map(int,p))
    min_palk=min(p)
    ind=p.index(min_palk)
    nimi=i[ind]
    print(f"{nimi}-l on kõige väiksem palk {min_palk}")