#
# days = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
# weekend = ('sobota', 'niedziela')
#
# for day in days:
#     if day in weekend:
#         print('jest weekend')
#     else:
#         print('do pracy')


# from PIL import Image
#
# image : Image.Image = Image.open('/home/kursant/Desktop/dolar.jpg')  ##konstrukcja z : jest opcjonalna
# image = image.resize((2000,1000))
# image = image.rotate(90)
# image.save('/home/kursant/Desktop/dolarmini.jpg')
#
# import requests
# wp_page = requests.get('https://www.wp.pl/')
# print(wp_page.text)
#
# wp_page = requests.get()

# import requests
#
# api_key = '800101cc05e0bcd5b88c816246c988ff'
# api_host = 'http://api.openweathermap.org/data/2.5/weather'
# city = 'Gdansk'
#
# result = requests.get(f'{api_host}?appid{api_key}&q={city}')
#
# dict = result.json()
# print(f'temperatura: {dict['main']['temp']}')
#
# pass



# import requests
# ##zadanko combo
# from bs4 import BeautifulSoup
#
# page = requests.get('https://wallpaperlist.com/')
#
# parser = BeautifulSoup(page.content, 'html.parser')
#
# images = parser.find_all('img')
#
# for image in images:
#     print(image['src'])
#



#
# list_var = page.split('/')
# resource = page.open(list_var[0] + "//" + list_var[2] + image.get['src'])
# output = open(image.get(['src’].split(‘/‘)[-1],”wb")
# images.save('/home/kursant/Pictures')
# images = images.resize((64,proporcja))
# print('znaleziono: %s obrazków') % len(images)






# from urllib.request import urlopen
# url = "https://wallpaperlist.com/wave-sea-blue-water-nature-10852/"
# html = urlopen(url)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html)
# for res in soup.findAll('img'):
#     print(res.get('src'))
#     list_var = url.split('/')
#
# image_adress = (list_var[0]+"//"+list_var[2]+res.get('src')
#     resource = image_adress
#     output = open(res.get(('src’.split(‘/‘)[-1],”wb")
#   # output.write(resource.read('/home/kursant/Pictures'))
#   # print('znaleziono: %s obrazków') % len(images)
#
#     print(list_var[0]+"//"+list_var[2]+res.get('src'))


# import os
# from bs4 import BeautifulSoup
# import requests
# from PIL import Image
# from io import BytesIO
# import smtplib
# from email.mime.text import MIMEText
#
# page = requests.get('https://wallpaperlist.com/')
# parser = BeautifulSoup(page.content, 'html.parser')
# images = parser.find_all('img')
#
#
# licznik_zdjec = 0
# inne_formaty = 0
#
# for image in images:
#     link = image['src']
#     url = f"https://wallpaperlist.com/{link}"
#
#     response = requests.get(url)
#     image = Image.open(BytesIO(response.content))
#     nazwa = url.split("/")
#     format_pliku = url[-3:]
#
#     if format_pliku == "jpg":
#         nazwa = nazwa[8]
#         image.save(f"images\{nazwa}")
#         image = image.resize((64, 64))
#         image.save(f"images\\mini\{nazwa}")
#         licznik_zdjec = licznik_zdjec + 1
#
#     else:
#         inne_formaty = inne_formaty + 1
#
#
# pliki_oryginalne = os.listdir("images")
# ile_zdjec_o = 0
# rozmiar_oryginal = 0
# suma_rozmiar_oryginal = 0
#
# for zdjecie in pliki_oryginalne:
#     if zdjecie[-3:] == "jpg":
#         rozmiar_oryginal = os.path.getsize(f"images\\{zdjecie}")
#         oryginal_MB = rozmiar_oryginal / 1024 ** 2
#         ile_zdjec_o = ile_zdjec_o + 1
#         suma_rozmiar_oryginal = suma_rozmiar_oryginal + oryginal_MB
# suma_rozmiar_oryginal = "%0.2f" % suma_rozmiar_oryginal
#
# #
# #
# #

indeks = 4
for litera in 'Kotek':
    print('Litera nr {} to {}'.format(indeks,litera))
    indeks +=3

