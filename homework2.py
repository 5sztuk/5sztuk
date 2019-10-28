#1
# jaka_temperatura = input("jeśli chcesz przeliczyć na Fahrenheit wpisz F, jeśli na Celsjusz wpisz C").upper()
# if jaka_temperatura == "F":
#     Celsjusz = int(input("Podaj wartość w Celsjuszach"))
#     Fahrenheit = Celsjusz * 1.8 + 32
#     print(Fahrenheit, "F")
# if jaka_temperatura == "C":
#     Fahrenheit = int(input("Podaj wartość w Fahrenheitach"))
#     Celsjusz = (Fahrenheit - 32) * 5.0/9.0
#     print(Celsjusz, "C")
# else:
#     print("nie podałeś F ani C")

#2
# liczba = input("podaj liczbę")
# print('pierwsza cyfra z twojej liczby to ' + liczba[0])
# print('ostatnia cyfra z twojej liczby to ' + liczba[-1])

#3
# n=int(input("podaj długość prostokąta: "))
# m=int(input("podaj szerokość prostokąta: "))
# c="-"
# def print_rect(n, m, c):
#     for a in range(m):
#         print (n*c)
# print_rect(n, m, c)

#4
# liczba_bin = input("podaj liczbę binarną:")
# liczba_dec = int(liczba_bin, 2)
# print(liczba_dec)

#5
# print("czy rok jest przestępny?")
# rok_przestepny = int(input("Podaj rok: "))
# if rok_przestepny % 4 == 0:
#     print("rok jest przestępny")
# else:
#     print("podany rok nie jest przestępny")

#6


#7
# kwota_PLN = float(input("podaj kwotę do rozmienienia: "))
#
# if kwota_PLN <= 0:
#     print("Błąd - nie rozmienisz pieniędzy, których nie masz ;)")
# else:
#     piatki = kwota_PLN // 5
#     dwojki = (kwota_PLN % 5) // 2
#     jedynki = (kwota_PLN % 5 % 2) // 1
#     piedziesieciogroszowki = (kwota_PLN % 5 % 2 % 1) // 0.5
#     dwudziestogroszowki = (kwota_PLN % 5 % 2 % 1 % 0.5) // 0.2
#     dziesieciogroszowki = (kwota_PLN % 5 % 2 % 1 % 0.5 % 0.2) // 0.1
#
# print("kwota", kwota_PLN, "składa się z: ")
# print("piątki: ", piatki)
# print("dwójki: ", dwojki)
# print("jedynki: ", jedynki)
# print("piędziesięciogroszówki", piedziesieciogroszowki)
# print("dwudziestogroszówki", dwudziestogroszowki)
# print("dziesięciogroszówki", dziesieciogroszowki)

#8
# h_pir = int(input("podaj wysokość piramidy"))
# for i in range (0, h_pir):
#     for j in range(0, h_pir-i-1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("#", end=" ")
#     print()

#9
# wiek_psa = int(input("podaj wiek twojego psa: "))
# if wiek_psa <=2:
#     ludzki_wiek_psa = wiek_psa*10.5
#     print(ludzki_wiek_psa)
# elif wiek_psa >2:
#     ludzki_wiek_psa = 21 + (wiek_psa-2)*4
#     print(ludzki_wiek_psa)

#10