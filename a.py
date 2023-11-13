# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:43:03 2023

@author: student
"""
def wyswietl_imiona(imiona):
    if len(imiona) != 5:
        print("Lista powinna zawierać 5 imion.")
        return
    for imie in imiona:
        print(imie)


wyswietl_imiona(["Basia", "Bartek", "Marta", "Filip", "Dominika"])

