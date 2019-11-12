#programik statystyki dla tadzio.txt

with open('statystyki.txt', 'a+') as file:
    file.seek(0)
    linijka = file.readline()
    linijka = linijka[29:]
    linijka_liczba = int(linijka)+1
    file.truncate(29)
    file.write(f'{linijka_liczba}')
    print(f'ilość uruchomień: {linijka_liczba}')

with open('tadzio.txt', 'r+') as tadzio:
    tadzio = tadzio.read()
    licznik_zdan = tadzio.count('.')
    ile = f'zdań jest {licznik_zdan}'
    print(ile)

with open('statystyki.txt', 'a+') as file:
    file.write(f'\n{ile}')

    podzial = tadzio.split()
    licznik_slow = len(podzial)
    ile_slow = f'słów jest {licznik_slow}'
    print(ile_slow)

with open('statystyki.txt', 'a+') as file:
    file.write(f'\n{ile_slow}')

##to Pan Tadeusz - tam nie ma liczb ;)

licz_liczby = 0
for slowo in podzial:
    for znak in slowo:
        cyfra = 0
        if znak.isdigit() is True:
            cyfra += 1
    if cyfra >= 1:
        licz_liczby += 1

licz_liczby = f'liczb jest {licz_liczby}'
print(licz_liczby)

with open('statystyki.txt', 'a+') as file:
    file.write(f'\n{licz_liczby}')