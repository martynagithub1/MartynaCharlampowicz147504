def wyswietl_imiona(imiona):
    if len(imiona) != 5:
        print("Lista powinna zawierać 5 imion.")
        return
    for imie in imiona:
        print(imie)


wyswietl_imiona(["Martyna", "Dawid", "Kacper", "Ewa", "Zosia"])
