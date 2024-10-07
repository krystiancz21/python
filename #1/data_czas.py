from datetime import datetime

def informacje_o_dacie():
    teraz = datetime.now()
    
    # a. data i czas
    print(f"Data i czas: {teraz}")
    
    # b. procent dnia
    sekundy_w_dniu = teraz.hour * 3600 + teraz.minute * 60 + teraz.second
    procent_dnia = (sekundy_w_dniu / 86400) * 100
    print(f"Procent dnia: {procent_dnia:.2f}%")
    
    # c. procent miesiąca
    dni_w_miesiacu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if teraz.month == 2 and ((teraz.year % 4 == 0 and teraz.year % 100 != 0) or (teraz.year % 400 == 0)):
        dni_w_miesiacu[1] = 29
    procent_miesiaca = (teraz.day / dni_w_miesiacu[teraz.month - 1]) * 100
    print(f"Procent miesiąca: {procent_miesiaca:.2f}%")
    
    # d. procent roku
    dzien_roku = teraz.timetuple().tm_yday
    dni_w_roku = 366 if teraz.year % 4 == 0 and (teraz.year % 100 != 0 or teraz.year % 400 == 0) else 365
    procent_roku = (dzien_roku / dni_w_roku) * 100
    print(f"Procent roku: {procent_roku:.2f}%")

if __name__ == "__main__":
    informacje_o_dacie()