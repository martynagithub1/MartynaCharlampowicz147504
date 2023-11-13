
def polacz_i_poteguj(list1, list2):
    polaczona_lista = list(set(list1 + list2))
    wynikowa_lista = [x ** 3 for x in polaczona_lista]
    return wynikowa_lista

wynik = polacz_i_poteguj([1, 2, 3], [2, 3, 4])  
print(wynik)