import random


# Generujemy 4 cyfry z zakresu
def generate_num():
    num = random.randint(1000, 9999) # Generujemy liczbe z zakresu od 1000 do 9999 - polecenie zadania
    num = 1235

    return list(str(num)) # zwracamy listę tych liczb jako stringi


# Krowy
def numOfCows(losowa_liczba, liczba_uzytkownika):
    cow = 0  # licznik krów

    for i in range(len(losowa_liczba)): # liczymy losowe liczby w zakresie
        if losowa_liczba[i] == liczba_uzytkownika[i]: # dla kazdej liczby losowej jesli trafi na liczbe uzytkownika
            cow += 1  # dodajemy krowe
            losowa_liczba[i] = 'x'  # oznaczamy liczbe losowe jako x
            liczba_uzytkownika[i] = 'y'  # oznaczamy liczbe_uzytkownika jako y
    return cow, losowa_liczba, liczba_uzytkownika
    # zwracamy licznik krow, losoweliczbe, liczbe uzytkownika


# Byki
def numOfBull(losowa_liczba, liczba_uzytkownika):
    bull = 0  # licznik bykow

    for i in range(len(losowa_liczba)): # liczymy losowe liczby w zakresie
        for j in range(len(losowa_liczba)): # jeszcze raz liczymy jako druga petla
            if liczba_uzytkownika[i] == losowa_liczba[j]: # jesli liczba uzytkownika jest w puli wylosowanych
                # ale nie trafi dokladnie w cel czyli nie jest liczba losowa[i] bo i to krowy
                bull += 1  # dodaj byka
                losowa_liczba[j] = 'x' # oznaczamy liczbe losowa jako x czyli nasze byki
                liczba_uzytkownika[i] = 'y' # oznaczamy liczbe uzytkownika
    return bull


def main():

    losowa_liczba = generate_num() # losowa liczba czyli nasz zakres liczb od 1000 9999
    losowa_liczba_kopia = losowa_liczba.copy() # robimy kopie liczby losowej aby znowu dostac wszystkie
    # 4 liczby dla uzytkownika, tak jakby odswiez, jak tego nie zrobimy zostana nam zabrane liczby ktore wczesniej juz uzylismy
    tries = 0 # licznik prob

    while True:
        print(losowa_liczba)
        print(losowa_liczba_kopia)
        liczba_uzytkownika = list(input("Podaj liczbę: "))

        Krowy, losowa_liczba, liczba_uzytkownika = numOfCows(losowa_liczba, liczba_uzytkownika)
        Byki = numOfBull(losowa_liczba, liczba_uzytkownika)
        print("Krowy:", Krowy, "Byki:", Byki)
        tries += 1

        if Krowy == 4:
            print("Wygrałeś! Koniec Gry!")
            print("Do osiągnięcia sukcesu potrzebowałeś tylko:", tries, "prób")
            break
        else:
            losowa_liczba = losowa_liczba_kopia.copy()
            # dla petli while znowu robimy odswiez


if __name__ == "__main__":
    main()
