class Krzeslo ():
    def __init__(self, kolor_siedziska = 'czerwony'):
        self.kolor_siedziska = kolor_siedziska
        self.ilosc_kol = 5
        self.wysokosc = '90cm'
        self.szerokosc = '40cm'
        self.glebokosc = '40cm'
        self.regulacja_wysokosci = True
        self.regulacja_podlokietnikow = False
        self.material = '100% cotton'

        pass
    def __str__(self):
        return f'krzeslo koloru {self.kolor_siedziska}'

obiekt = Krzeslo()
print(obiekt)
print(obiekt.kolor_siedziska)

obiekt = Krzeslo('niebieski')
print(obiekt)
print(obiekt.kolor_siedziska)