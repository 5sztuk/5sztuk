# lista = [1, 2, 3]
# nowa_lista = lista
# #kopia_listy = lista.copy()
# kopia_listy = lista[:]
# lista[0] = 'X'
#
# print (lista)
# print(nowa_lista)
# print(kopia_listy)
#
# import copy
# lista = [1,
#          2,
#          3,
#          ['A', 'B', 'C']
#          ]
#
# nowa_lista = lista
# kopia_listy = lista.copy()
# gleboka_kopia_listy = copy.deepcopy(lista)
# lista[0] = 'X'
# lista[3][0] = 'Y' #zamieniaA
#
# print (lista)
# print(nowa_lista)
# print(kopia_listy)
# print(gleboka_kopia_listy)

# def witaj():
#     print('cześć ziomku')
# #witaj()
# hi = witaj
# hi()


# def do_nothing(x, y, imie="Jola", wiek=22):
#     pass
# do_nothing(1)
# do_nothing(x=2, y=6, imie="Ola", wiek=23)
# do_nothing(2, 6)

##scope
def zmien_imie():
    if imie == "Teresa":
        return 'To twoje imie'
    else:
        return False
imie = zmien_imie('Teresa')
print(imie)




























