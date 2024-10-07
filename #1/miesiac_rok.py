def liczba_dni_w_miesiacu(miesiac, rok):
    if not (1800 <= rok <= 2200):
        raise ValueError("Rok musi być między 1800 a 2200")
    if not (1 <= miesiac <= 12):
        raise ValueError("Miesiąc musi być między 1 a 12")
    
    dni_w_miesiacu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if miesiac == 2 and ((rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0)):
        return 29
    else:
        return dni_w_miesiacu[miesiac - 1]

if __name__ == "__main__":
    print(liczba_dni_w_miesiacu(10, 2024))
