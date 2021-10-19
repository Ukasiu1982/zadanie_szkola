import sys

# klasa = []
# osoba = []
#
# while True:
#     wejscie = input()
#     if wejscie != "":
#         if wejscie == 'koniec':
#             if osoba:
#                 klasa.append(osoba)
#             break
#         elif wejscie in ['wychowawca', 'nauczyciel', 'uczen']:
#             if not osoba:
#                 osoba.append(wejscie)
#             else:
#                 klasa.append(osoba)
#                 osoba = [wejscie]
#            else:
#                osoba.append(wejscie)
# print(klasa)


class Wychowawca:
    def __init__(self):
        self.name = None
        self.klasy = []

    def wczytaj(self):
        self.name = input()
        while True:
            klasa = input()
            if not klasa:
                break
            self.klasy.append(klasa)

    def wypisz(self):
        print("Wychowawca {}, {} ".format(self.name, self.klasy))


class Nauczyciel:
    def __init__(self):
        self.name = None
        self.przedmiot = None
        self.klasy = []

    def wczytaj(self):
        self.name = input()
        self.przedmiot = input()
        while True:
            klasa = input()
            if not klasa:
                break
            self.klasy.append(klasa)

    def wypisz(self):
        print("Nauczyciel {}, uczacy {}, klasy {} ".format(self.name, self.przedmiot,
                                                     self.klasy))

class Uczen:
    def __init__(self):
        self.name = None
        self.klasa = None

    def wczytaj(self):
        self.name = input()
        self.klasa = input()

    def wypisz(self):
        print("Uczen {}, klasa {} ".format(self.name, self.klasa))

class Klasa():
    def __init__(self):
        self.uczniowie = []


klasy = {}
uczniowie = []
nauczyciele = []
wychowawcy = []


while True:
    wejscie = input()
    if wejscie == 'koniec':
        break
    elif wejscie == 'uczen':
        uczen = Uczen()
        uczen.wczytaj()
        uczniowie.append(uczen)
        if uczen.klasa in klasy.keys():
            klasy[uczen.klasa].append(uczen)
        else:
            klasy[uczen.klasa] = [uczen]
    elif wejscie == 'wychowawca':
        wychowawca = Wychowawca()
        wychowawca.wczytaj()
        wychowawcy.append(wychowawca)
    elif wejscie == 'nauczyciel':
        nauczyciel = Nauczyciel()
        nauczyciel.wczytaj()
        nauczyciele.append(nauczyciel)
    else:
        print('zle dane')
        break



akcja = sys.argv[1]

if len(akcja) > 2:
    for osoba in wychowawcy:
        if akcja == osoba.name:
            osoba.wypisz()
            for uczen in uczniowie:
                if uczen.klasa in osoba.klasy:
                    uczen.wypisz()
    for osoba in nauczyciele:
        if akcja == osoba.name:
            osoba.wypisz()
            for wychowawca in wychowawcy:
                print(set(wychowawca.klasy) & set(osoba.klasy))
    for uczen in uczniowie:
        if akcja == uczen.name:
            uczen.wypisz()
            for nauczyciel in nauczyciele:
                if uczen.klasa in nauczyciel.klasy:
                    nauczyciel.wypisz()
else:
    for wychowawca in wychowawcy:
        if akcja in wychowawcy.klasy:
            wychowawca.wypisz()
            for uczen in uczniowie:
                if akcja == uczen.klasa:
                    uczen.wypisz()




