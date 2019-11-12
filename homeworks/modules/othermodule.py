# print('Mój moduł')

def add(*args):

    sum = 0

    for number in (args):
        sum = sum + number

    return sum

#jeśli wywołujesz to w module to masz "main" a jeśli w programie to wyświetli ci się nazwa modulu
print(__name__)