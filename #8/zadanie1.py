import re

def check_number(number):
    """
    Funkcja sprawdza czy przekazana liczba jest liczbą zmiennoprzecinkową.
    
    Returns:
        - True, jeśli liczba jest liczbą zmiennoprzecinkową
        - False, jeśli liczba nie jest liczbą zmiennoprzecinkową
    """
    if re.match(r"^[+-]?\d+\.\d+$", str(number)):
        return True
    else:
        return False

if __name__ == "__main__":
    numbers = ["-123.456", "0.0", "+3.14", "42.42", "999", "999.0", "3.14159", "-0.001", "12345.67890", ".5", "-.8"]
    
    for number in numbers:
        print(f"Dla liczby [{number}] wynik to: {str(check_number(number))}")
