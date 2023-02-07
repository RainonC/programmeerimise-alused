#def loe_failist(file:str)->list:
#    """Loeme failist read ja lisame järjendisse 
#    :param str file: Faili nimetus
#    """
#    fail=open(file,'r',encoding="utf-8-sig")
#    mas=[]
#    for rida in fail:
#        if rida.isdigit():
#            mas.append(int(rida).strip())
#        else:
#            mas.append(rida.strip())
#    fail.close()
#    return mas

#def list_failisse(mas:list,file:str):
#    """Salvestamine loetelu failisse
#    :param str file: Faili nimetus
#    :param str mas: Loetelu
#    """
#    f=open(file,'w',encoding="utf-8-sig")
#    for item in mas:
#        f.write(item+"\n")
#    f.close()

#def elem_listisse(k:list,l:list):
#    """
#    """
#    k- kodanikud, l- linn

#    n=int(input("Mitu linna lisame? "))
#    for j in range(n):
#            nimi=input("Linn: ")
#            l.append(nimi)
#            k=input("Kodanikkud: ")
#            k.append(k)
#    print(k)
#    print(l)
#    return k,l

def populatsioon(linn, linnad):
    if linn in linnad.keys():
        return f'{linn} kodanikke arv on {linnad[linn]} inimest.'
    else:
        return 'Sellist linna ei ole.' 

def show_inf(cities):
    sorted_tuple = sorted(cities.items())
    return sorted_tuple

def most_pop(cities):
    big = 0
    town = ''
    for city, pop in cities.items():
        if pop > big:
            big = pop
            town = city
    return f'{town} : {big}'

def less(cities, num):
    my_dic = {}
    for city, pop in cities.items():
        if pop < num:
            my_dic[city] = pop
    return my_dic


