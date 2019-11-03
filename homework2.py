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
# wysokosc = "|"
# szerokosc = "-"
# l_szer = int(input("podaj szerokość prostokąta: "))
# l_wys = int(input("podaj wysokość prostokąta: "))
# print("+" + l_szer*szerokosc + "+")
# for i in range(0,l_wys):
#         print(wysokosc + l_szer*" " + wysokosc)
# print("+" + l_szer*szerokosc + "+")


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
# owoc1 = input("podaj 1. owoc")
# owoc2 = input("podaj 2. owoc")
# owoc3 = input("podaj 3. owoc")
# lista = [owoc1, owoc2, owoc3]
# # print("+" + len(owoc1)*"-" + "+" + len(owoc2)*"-" + "+" + len(owoc3)*"-" + "+")
# # print("|" + owoc1 + "|" + owoc2 + "|" + owoc3 + "|")
# # print("+" + len(owoc1)*"-" + "+" + len(owoc2)*"-" + "+" + len(owoc3)*"-" + "+")
# print("+" + 20*"-" + "+" + 20*"-" + "+" + 20*"-" + "+")
# print("|" + owoc1+(20-len(owoc1))*" " + "|" + owoc2+(20-len(owoc2))*" " + "|" + owoc3+(20-len(owoc3))*" " + "|")
# print("+" + 20*"-" + "+" + 20*"-" + "+" + 20*"-" + "+")

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

#10 ##dodaj zeby było 01 i zakraglenia przy temp (k, f, d nawiasy)
# dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"
#
# dane[0:4]
# dane[4:8]
# dane[8:12]
# dane[12:16]
# dane[16:20]
#
# for godzina in range(0,24):
#     poczatek_zakresu = godzina * 4
#     koniec_zakresu = poczatek_zakresu + 4
#     temp = int(dane[poczatek_zakresu:koniec_zakresu]) / 100
#     zero = ""
#     if godzina <=9:
#         zero = "0"
#     tab = ""
#     if temp <=18.5:
#         tab = "\t!"
#     elif temp <=20:
#         tab = "\t!!"
#     wiersz_string = "{}{}:00:\t {:.2f}\u00b0C{}".format(zero,godzina,temp,tab)
#     print (wiersz_string)