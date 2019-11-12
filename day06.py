# import csv
#
# # imie = 0
# # nazwisko = 1
# # adres = 2
# # tel = 3
# # wiek = 4
#
# with open('test.csv', 'r+') as csv_file:
#     csv_data = csv.reader(csv_file)
#
#     wiek_suma = 0
#
#     for row in csv_data:
#         if (row[4].isdigit()):
#             wiek = int(row[4])  ##zamiast 4 możesz dać zmienną wiek
#             wiek_suma = wiek_suma + wiek
#
#     print(wiek_suma)
#
#     csv_write = csv.writer(csv_file)
#     csv_write.writerow(['Łukasz', 'Falkowicz', 'Gdańsk', '28890001', '18'])


import pickle

entries = [
    {"title": "Pierwszy wpis", "body": "Treść pierwszego wpisu", "author": "Łukasz", "date": "2019-07-08"},
    {"title": "Drugi wpis", "body": "Treść drugiego wpisu", "author": "Łukasz", "date": "2017-09-08"}
]

with open('book.pkl', 'rb+') as book_file:  ##w nie zadziała bo to binarny tryb wiec trzeba dodac b --> wb, potem zmiana na rb+
    pickle.dump(entries, book_file)

    #data = pickle.load(book_file)
    #print(data)

title = input("podaj tytuł: ")
body = input("podaj wpis: ")
author = input("podaj imie: ")

nowy = {"title": title, "body": body, "author": author, "date": "2019-11-07"}

with open('book.pkl', 'rb+') as book_file:

    stare = pickle.load(book_file) #pobranie danych

    stare.append(nowy)

    counter = (len(stare))

    book_file.seek(0)

    pickle.dump(stare, book_file) #zapisuje

    print(counter)

    print("dziękuje")


try:
    division = 10/0
except:
    print("nie dziel przez zero sknero")
















