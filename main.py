import sys

klasa = []
osoba = []

while True:
    wejscie = input()
    if wejscie != "" :
        if wejscie == 'koniec':
            if osoba:
                klasa.append(osoba)
            break
        elif wejscie in ['wychowawca', 'nauczyciel', 'uczen']:
            if not osoba:
                osoba.append(wejscie)
            else:
                klasa.append(osoba)
                osoba = [wejscie]

        else:
            osoba.append(wejscie)
print(klasa)


class Wychowawca:
    def __init__(self, imie, nazwisko, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasy= []


class Nauczyciel:
    def __init__(self, imie, nazwisko, przedmiot, klasy):
        self.imie = imie
        self.nazwisko = nazwisko
        self.przedmiot = przedmiot
        self.klasy= []

class Uczen:
    def __init__(self, imie, nazwisko, klasa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.klasa = []