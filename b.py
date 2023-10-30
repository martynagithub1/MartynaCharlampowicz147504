# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:56:13 2023

@author: student
"""

#1sposob
def pomnoz_przez_dwa(liczby):
    if len(liczby) != 5:
        print("Lista musi zawierać 5 liczb.")
        return
    wynik = []
    for liczba in liczby:
        wynik.append(liczba * 2)
    return wynik

print(pomnoz_przez_dwa([1, 2, 3, 4, 5]))

#pętla składana
def pomnoz_przez_dwa_lista_składana(liczby):
    if len(liczby) != 5:
        print("Lista musi zawierać 5 liczb.")
        return
    return [liczba * 2 for liczba in liczby]


print(pomnoz_przez_dwa_lista_składana([1, 2, 3, 4, 5]))