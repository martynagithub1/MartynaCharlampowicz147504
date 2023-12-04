def wyswietl_co_drugi_element(lista):
    if len(lista) != 10:
        print("Lista musi zawierać dokładnie 10 elementów")
        return

    for i in range(1, len(lista), 2):
        print(lista[i])


lista = list(range(10))
wyswietl_co_drugi_element(lista)
