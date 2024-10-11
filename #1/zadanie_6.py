def is_year_leap(year):
    if year < 1800 or year > 2200:
        raise Exception("Rok musi być w przedziale od 1800 do 2200.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(month, year):
    if month < 1 or month > 12:
        return "Niepoprawny numer miesiąca"
    
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    else:
        return days_in_months[month - 1]
    
from datetime import datetime
now = datetime.now()
print(f"Ile dni ma obecny miesiąc: {days_in_month(now.month, now.year)}")
print(f"Ile dni ma obecny miesiąc: {days_in_month(2, now.year)}")
print(f"Ile dni ma 3 miesiąc 1948 roku: {days_in_month(7, 1938)}")
print(f"Ile dni ma 2 miesiąc 2024 roku: {days_in_month(1, 2023)}")