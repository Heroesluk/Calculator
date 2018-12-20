



def kalkulator():
    print("Kalkulator \n Dostepne funkcje: \n Dodawanie \n Odejmowanie \n Dzielenie \n Mnozenie \n exit = zakonczenie programu")

def liczby():

    try:
        val = float(raw_input())
    except ValueError:
        print("Najpierw liczba")

    x = raw_input()

    try:
        vav = float(raw_input())
    except ValueError:
        print("Najpierw liczba")


    if (x == '+'):
        wat=val + vav
        print(wat)

    elif (x == '-'):
        wat = val - vav
        print(wat)

    elif (x == '*'):
        wat = val * vav
        print(wat)

    elif (x == '/'):
        wat = val / vav
        print(wat)

    while (True):
        x = raw_input()
        if(x=='exit'):
            break
        try:
            vav = float(raw_input())
        except ValueError:
            print("Najpierw liczba")

        if (x == '+'):
            wat = wat + vav
            print(wat)

        elif (x == '-'):
            wat = wat - vav
            print(wat)

        elif (x == '*'):
            wat = wat * vav
            print(wat)

        elif (x == '/'):
            wat = wat / vav
            print(wat)


















kalkulator()

liczby()






