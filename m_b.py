# морской бой
# версия 1,1
def zapolnit(spisok, simbol, razmer):
    i = 0
    j = 0
    while j < razmer:
        nev = []
        i = 0
        while i < razmer:
            new.append(simbol)
            i += 1
        spisok.append(nev)
        j += 1
def pokazat(spisok, razmer):
    i = 0
    while i < razmer:
        print(spisok [i])
        print()
        i = i + 1
pole = []
karta = []
razmer = int(input("Введите размер таблицы:"))
zapolnit(pole,0, razmer)
zapolnit(karta,".", razmer)
pokazat(pole, razmer)
print()
pokazat(karta, razmer)

