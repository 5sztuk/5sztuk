#tutaj wykonujesz, a modul masz w innym py - mymodule

#trzy formy importu modułu
#rób zawsze importy na początku pliku żeby widzieli je programisci
# import mymodule
#
# from mymodule import hello as helloFromModule
#
# import homeworks.modules.othermodule as othermodule
#
# # def hello():
# #     print('dzień dobry')
# #
# # mymodule.hello()
# #
# # hello()
# #
# # helloFromModule()
#
# result = othermodule.add(1, 2, 45, 12)
# # print(result)
#
# ##tworzenie nowego pliku na dysku i wrzucenie go do kosza
# import os
# try:
#     os.mknod('plik do usuniecia.txt')
# except FileExistsError:
#     print('plik już istnieje')
#
# #import send2trash ##trzeba zainstalowac bo nie dziala
# os.mknod('plik do usuniecia.txt')
# ##działa tylko na linux. na windows bedzie to funkcja open()
# #send2trash.send2trash('plik do usunięcia.txt')


##programik który wysła maila

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = input('podaj temat')
body = input('podaj tresc')
recipient = input('podaj adresata')

mail_body = MIMEText(body)

mail = MIMEMultipart()  ##utworzenie wydmuszki maila, wie gdzie go skleic
mail['subject'] = subject
mail['from'] = 'prezydent Polski <isapy@int.pl>'
mail['to'] = recipient
mail.attach(mail_body)

server = smtplib.SMTP('poczta.int.pl')
server.starttls()   #uruchomienie szyfrowanego polaczenia
server.login('isapy@int.pl', 'isapython;')
server.send_message(mail)
server.quit()






















