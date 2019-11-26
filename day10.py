# import datetime
#
# class Pizza():
#
#     stawka_VAT = 23
#     __marza = 1.05  ##to jest pole prywatne
#
#     def __init__(self, skladnik_glowny = None):
#         self.skladnik_glowny = skladnik_glowny
#         self.rozmiar = '30cm'
#         self.ciasto = 'cienkie'
#         self.cena = 100 * Pizza.__marza
#
#     @classmethod
#     def Hawajska(cls):
#         return cls('ananas')
#
#     @classmethod
#     def podaj_VAT(cls):
#         return cls.stawka_VAT
#
# ##metoda statyczna da przykładu
#
#     @staticmethod
#     def podaj_date():
#         return datetime.datetime.now().strftime('%Y-%d-%m')
#
# # hawajska = Pizza('ananas')
# # print(hawajska.skladnik_glowny)
# # hawajska = Pizza.Hawajska()
# # print(hawajska.skladnik_glowny)
# # print(Pizza.podaj_VAT())
# # print(Pizza.podaj_date())
#
#
# ##def to metoda obiektu tym bardziej jeśli ma self
#
# print(Pizza.stawka_VAT)
# #print(Pizza.__marza) ##to jest pole pryw wiec w taki sposob sie do niego nie dostaniesz, ale jeśli jesteś w KLASIE to ją widzisz
# # ale możesz tak
# print((Pizza._Pizza__marza) ##prywatnosc jest ale jest ona pseudo bo mozna to obejsc
# # pizza = Pizza()
# # print(pizza.cena)
#
# print(Pizza.__dict__)  ##tutaj python doda Pizza do __marza
#
#
# ##setter gdy wpiszemy np "cena ="
#
# ##getter - służy do zwrocenia wartosci ze zmniennej self.__imie

# ##deleter usuwa/aktualizuje

import datetime
class Student():

    def __init__(self):
        self.__imie = None
        self.nazwisko = None
        self.data_dodania = None
        self.data_usuniecia = None

    @property  ##dodaj __ do selfów bo inaczej się pogubi
    def imie(self):
        return self.__imie.capitalize()

    @imie.setter
    def imie(self, wartosc):
        self.__imie = wartosc

    @imie.deleter
    def imie(self):
        self.skasowany = True
        self.data_dodania


student = Student()
student.imie = 'łukasz'
student.nazwisko = 'falkowicz'
student.data_dodania = datetime.datetime.now().strftime('%Y-%d-%m')

print(student.imie)
print(student.nazwisko)
print(student.data_dodania)
print(student.data_usuniecia)










































