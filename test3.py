# Import daty
from datetime import date

# Obecny rok i miesiąc
a = date.today().year
e = date.today().month
liczba_dzieci = int(input('Podaj liczbę dzieci, które nie skończyły 18 lat: '))
suma_lat = []
suma_miesiecy = []
for i in range(liczba_dzieci):
    print('Podaj rok urodzenia dziecka', i + 1, ':')
    rok_urodzenia = int(input())
    while (a - rok_urodzenia) < 0 or (a - rok_urodzenia) >= 18:
        print('Wiek dziecka jest poza skalą 18 lat. Wprowadź poprawną datę lub zmniejsz liczbę dzieci.')
        rok_urodzenia = int(input('Podaj rok urodzenia dziecka: '))
        if (a - rok_urodzenia) > 0 and (a - rok_urodzenia) < 18:
            break
    print('Podaj miesiąc urodzenia dziecka', i + 1, '(od 1 do 12):')
    mount = int(input())
    while mount < 1 or mount > 12:
        print('!Podano wartość z poza przedziału!')
        print('Podaj miesiąc urodzenia dziecka', i + 1, '(od 1 do 12):')
        mount = int(input())
        if mount >= 1 and mount <= 12:
            break
    suma_lat.append(rok_urodzenia)
    suma_miesiecy.append(mount)
for i in suma_lat:
    min = None
    if min == None or min < i:
        min = i
print(min)
print('Otrzyamsz jeszcze ~', (18 * (i + 1) - (a * (i + 1) - sum(suma_lat))) * 12 * 500 - (e * (i + 1) * 500 + sum(suma_miesiecy) * (i + 1) * 500), ' zł')
input()
