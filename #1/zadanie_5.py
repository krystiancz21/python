import calendar

def check_year(year): 
    return(calendar.isleap(year)) 

def leap_year(year):
    if year < 1800 or year > 2200:
        raise Exception("Rok musi być w przedziale od 1800 do 2200.")

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True  
    else:
        return False    

print("Sprawdzenie:")
print(check_year(1900))
print(check_year(2024))

print("\nFunkcja")
print(leap_year(1900))
print(leap_year(2024))
print(leap_year(1))