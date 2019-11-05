
# contacts = {
#     "names" : ['Ala', 'Ola', 'Jan'],
#             "surnames" : ['Kowalski', 'Malinowska', 'Igrekowski'],
#             "cities" : ['Gdańsk', 'Sopot', 'Gdynia']
# }
#
# # print(contacts['cities'])
# # contacts['cities'].append('Rumia')
# # print(contacts)
# #
# contacts.update({'countries': ['Polska', 'USA', 'Dania']})
# # print(contacts)
# # print(len(contacts))
# # print(contacts.items()) ##zwraca krotki
#
# for key, value in enumerate(contacts['names']):
#     #print(key, value)
#     name = value
#     surname = contacts['surnames'][key]
#     city = contacts['cities'][key]
#     country = contacts['countries'][key]
#     print(f"{name} {surname} mieszka w {city} ({country})")



#
# contacs = {
#     "0": {"name": "Ala", "surname": "Kowalska", "cities": "Gdańsk"},
#     "1": {"name": "Ola", "surname": "Malinowska", "cities": "Gdynia"},
#     "2": {"name": "Jan", "surname": "Igrekowski", "cities": "Rumia"}
# }
# for key, value in enumerate(contacs):
#     # print(key)
#     # print(contacs[str(key)]["name"])
#     imie = (contacs[str(key)]["name"])
#     naz = (contacs[str(key)]["surname"])
#     mias = (contacs[str(key)]["cities"])
#     print(imie + " " + naz + " mieszka w" + " " + mias) ##TO WCIĘCIE MA ZNACZENIE!!!




#
# file = open('file.txt', 'w')
# file.write('zapisz coś')
# file.close()



# with open('file.py', 'w+') as file:  ##jeśli wezmiemy 'a' to kursor ustawi sie na koncu bo jest to tryb do dopisywania
#     #print(file.tell())
#     file.write('cosik')
#     file.writelines(['\nwiersz 1'])
#     #print(file.tell())
#     file.write('\ni jeszcze coś')
#     file.seek(0)  ##wracamy do początku pliku kursorem seek żeby przeczytał całość
#     print(file.read())



#programik liczący ile razy uruchomiono plik
x =

file = open('file.txt', 'w')
file.write('zapisz coś')
file.close()

print('cześc, uruchmiłes plik x razy')























