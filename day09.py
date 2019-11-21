# class Stol():
#     def __init__(self):
#         self.ilosc_nog = 4
#
#     def __add__(self, other):
#         return self.ilosc_nog + other.ilosc_nog
#
# class Krzeslo ():
#     def __init__(self, kolor_siedziska = 'czerwony', cena = 100):
#         self.kolor_siedziska = kolor_siedziska
#         self.ilosc_kol = 5
#         self.wysokosc = 90
#         self.szerokosc = 40
#         self.glebokosc = 40
#         self.regulacja_wysokosci = True
#         self.regulacja_podlokietnikow = False
#         self.material = '100% cotton'
#         self.cena = cena
#         self.vat = 23
#         self.ilosc_nog = 5
#
#         pass
#     def __str__(self):
#         return f'krzeslo koloru {self.kolor_siedziska}'
#
#     def __len__(self):
#         return self.wysokosc * self.szerokosc * self.glebokosc
#
#     def pobierz_cene_netto(self):
#         return self.cena
#
#     def pobierz_cene_brutto(self):
#         return self.cena * (1 + self.vat/100)
#
# krzeslo = Krzeslo()
# print(krzeslo)
# stol = Stol()
# print(stol)
#
# print(stol + krzeslo)
#
#
# # obiekt = Krzeslo()
# # print(obiekt)
# # print(obiekt.kolor_siedziska)
# #
# # obiekt = Krzeslo('niebieski')
# # print(obiekt)
# # print(obiekt.kolor_siedziska)
# # print(len(obiekt))
# #
# # obiekt2 = Krzeslo('zielone', 120)
# # print(obiekt2.pobierz_cene_netto())
# # print(obiekt2.pobierz_cene_brutto())
# # print(obiekt2.cena * 1.22)



class Zwierze:
    def __init__(self):
        self.oczy = 2
        self.wlosy = True
    def __str__(self):
        return f'Oczy: {self.oczy}, włosy: {self.wlosy}'

class Czlowiek(Zwierze):
    def dajglos(self):
        print('Heee')

class Student(Czlowiek):
    def dajglos(self):
        print('siema jestem student')

class Kot(Zwierze):
    def dajglos(self):
        print('miau')

class Pies(Zwierze):
    def dajglos(self):
        print('łuf łuf')

class Bokser(Pies):
    pass

class Jamnik(Pies):
    pass

class Dresiarz(Czlowiek):
    def __init__(self):
        super().__init__()  #działa tak że bierze poziom do góry, nie nadpisałby wartości
        self.wlosy = False

    def dajglos(self):
        super().dajglos()
        print('masz jakiś problem')

#
# zwierze = Zwierze()
#
# czlowiek = Czlowiek()
# czlowiek.dajglos()
#
# pies = Pies()
#
# kot = Kot()
#
# jamnik = Jamnik()
# jamnik.dajglos() #z psa
# print(jamnik.oczy) #ze zwierzecie

dresiarz = Dresiarz()
dresiarz.dajglos()
print('nie mam')
print(dresiarz)











