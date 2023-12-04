def wyswietl_parzyste_elementy(lista):
    if len(lista) != 11:
        print("Lista musi zawierać dokładnie 10 elementów")
        return

    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)


lista = list(range(11))
wyswietl_parzyste_elementy(lista)
