# Import daty
from datetime import date

# Obecny rok i miesiąc
a = date.today().year
e = date.today().month
# Liczba dzieci
try:
    liczba_dzieci = int(input('Podaj liczbę dzieci, które nie skończyły 18 lat: '))
except:
    liczba_dzieci = int(input('Podaj liczbę dzieci, które nie skończyły 18 lat: '))
    pass



# # Liczba dzieci mniejsza niż 2
# if liczba_dzieci >= 0 and liczba_dzieci <= 1:
#     print('Nie dostaniesz pieniędzy chyba, że masz więcej niż dwójkę dzieci poniżej 18 lat.')
#     wiecej_dzieci = str(input('Masz więcej niż dwójkę dzieci? (tak/nie)'))
#     # Każda inna odpowiedź niż tak/nie
#     while wiecej_dzieci != 'tak' and wiecej_dzieci != 'nie':
#         wiecej_dzieci = str(input('Masz więcej niż dwójkę dzieci? (tak/nie)'))
#         if wiecej_dzieci == 'tak':
#             liczba_dzieci = int(input('Podaj liczbę dzieci: '))
#             if liczba_dzieci > 1:
#                 break
#             while liczba_dzieci <= 1:
#                 print('Musisz podać liczbę większą lub równą 2')
#                 liczba_dzieci = int(input('Podaj liczbę dzieci: '))
#             if liczba_dzieci > 1:
#                 break
#         elif wiecej_dzieci == 'nie':
#             input('Zamknij program')
#             break
#             # Odpowiedź twierdząca
#     while wiecej_dzieci == 'tak':
#         liczba_dzieci = int(input('Podaj liczbę dzieci: '))
#         if liczba_dzieci > 1:
#             break
#         while liczba_dzieci <= 1:
#             print('Musisz podać liczbę większą lub równą 2')
#             liczba_dzieci = int(input('Podaj liczbę dzieci: '))
#         if liczba_dzieci > 1:
#             break
#     # Odpowiedź przecząca
#     while wiecej_dzieci == 'nie':
#         input('Zamknij program')
# # Liczba dzieci równa/większa 2
# suma_lat = []
# suma_miesiecy = []
# for i in range(liczba_dzieci):
#     print('Podaj rok urodzenia dziecka', i + 1, ':')
#     rok_urodzenia = int(input())
#     while (a - rok_urodzenia) < 0 or (a - rok_urodzenia) >= 18:
#         print('Wiek dziecka jest poza skalą 18 lat. Wprowadź poprawną datę lub zmniejsz liczbę dzieci.')
#         rok_urodzenia = int(input('Podaj rok urodzenia dziecka: '))
#         if (a - rok_urodzenia) > 0 and (a - rok_urodzenia) < 18:
#             break
#     print('Podaj miesiąc urodzenia dziecka', i + 1, '(od 1 do 12):')
#     mount = int(input())
#     while mount < 1 or mount > 12:
#         print('!Podano wartość z poza przedziału!')
#         print('Podaj miesiąc urodzenia dziecka', i + 1, '(od 1 do 12):')
#         mount = int(input())
#         if mount >= 1 and mount <= 12:
#             break
#     suma_lat.append(rok_urodzenia)
#     suma_miesiecy.append(mount)
# print('Otrzyamsz jeszcze ~', (18 * (i + 1) - (a * (i + 1) - sum(suma_lat))) * 12 * 500 - (
#         e * (i + 1) * 500 + sum(suma_miesiecy) * (i + 1) * 500), ' zł')
# input()
