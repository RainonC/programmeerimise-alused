def Kontroll(isikukood:str):
    """ Isikukoodi kontroll number
    On vaja isikukood sisestada
    :param str ik: Inimese isikukood
    :rtype: var Märamata tüüp
    """
    ik_l=list(isikukood)
    s = 0
    for i in range(0,10):                  
       s+=(i%9+1)*int(ik_l[i]) 
       print(f"{i%9+1}*{int(ik_l[i])}+", end="")
    print(s)
    s=s-(s//11)*11 
    print(s)
    if s==int(ik_l[10]):
       vastus = s
    else:
       vastus = "Kontrollnumber on vale "
    return vastus 
def Haigla(ik3:int):
    """Haigla 3 isikukoodi numbri alusel
    :param int ik3:
    :rtype: str Haigla ja koht
    """
    if ik3>1 and ik3<=10:
       haigla = "Kuressaare"
    elif ik3>10 and ik3<=19:
       haigla = "Tartu"
    elif ik3>19 and ik3<=220:
       haigla = "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    elif ik3>220 and ik3<=270:
       haigla = "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
    elif ik3>270 and ik3<=370:
       haigla = "Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla"
    elif ik3>370 and ik3<=420:
       haigla = "Narva Haigla"
    elif ik3>420 and ik3<=470:
       haigla = "Pärnu Haigla"
    elif ik3>470 and ik3<=490:
       haigla = "Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
    elif ik3>490 and ik3<=520:
       haigla = "Järvamaa Haigla (Paide)"
    elif ik3>520 and ik3<=570:
       haigla = "Rakvere, Tapa haigla"
    elif ik3>570 and ik3<=600:
       haigla = "Valga Haigla"
    elif ik3>600 and ik3<=650:
       haigla = "Viljandi Haigla"
    else:
       haigla = "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
    return haigla
def Sugu(ik1:int)->str:
    """

    """
    if ik1%2:
        sugu = "Naine"
    else:
        sugu= "Mees"
    return sugu
