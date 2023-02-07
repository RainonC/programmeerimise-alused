def loe_failist(file:str)->list:
    """Loeme failist read ja lisame j�rjendisse 
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
    """N�itab maksimaalse palga listis
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
    """N�itab minimaalse palga listis
    """
    p=list(map(int,p))
    min_palk=min(p)
    ind=p.index(min_palk)
    nimi=i[ind]
    print(f"{nimi}-l on k�ige v�iksem palk {min_palk}")

def sorteerimine(p:list, inimesed:list, a:int):
    N=len(p)
    p=list(map(int,p))
    if a==0:
        for i in range(0,N-1):
            for j in range(i+1,N):
                if p[i]<p[j]:
                    abi=p[i]
                    p[i]=p[j]
                    p[j]=p[i] 
                    abi=inimesed[i]
                    inimesed[i]=inimesed[j]
                    inimesed[j]=abi
    else:
        for i in range(0,N-1):
            for j in range(i+1,N):
                if p[i]>p[j]:
                    abi=p[i]
                    p[i]=p[j]
                    p[j]=p[i] 
                    abi=inimesed[i]
                    inimesed[i]=inimesed[j]
                    inimesed[j]=abi
    return p,inimesed

