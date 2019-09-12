import random



lista_z_wynikami = []
def toto():
    lista = [1, 14, 17, 31, 32, 44]          #liczby wpisz tu
    wynik = random.sample(range(1, 50), 6)
    lista_z_wynikami.extend(wynik)
    trafione = []
    for element in lista:
        if element in wynik:
            trafione.append(element)
    #print(sorted(wynik))
    if len(trafione) >= 3:
        print(f"Lotto : {trafione}")




def euro_lotto():
    lista2 = [4,18,30,31,45]
    lista3 = [1,6]
    wynik1 = random.sample(range(1,50), 5)
    wynik2 = random.sample(range(1,10), 2)
    trafione2 = []
    trafione3 = []
    for element2 in lista2:
        if element2 in wynik1:
            trafione2.append(element2)
    for element3 in lista3:
        if element3 in wynik2:
            trafione3.append(element3)
    print(sorted(wynik1), sorted(wynik2))
    if len(trafione2) > 3 and len(trafione3)>1:
         print(f"Eutolotto: {trafione2} {trafione3}")




for z in range(2):
    euro_lotto()

for i in range(2000):
    toto()

#for x in range(1, 50):
#    print(f"{x} wystąpiło : {lista_z_wynikami.count(x)} razy")

#count = wynik.count(i)
#print('ilość trafionych : ', count)





