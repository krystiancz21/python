import re

class Order:
    @staticmethod
    def check_name(name):
        if not name[0].isupper():
            return False
        return True
    
    @staticmethod
    def check_surname(surname):
        r = re.compile(r"[A-ZŁŹŻĆŚŃÓĘĄ][a-złźćśńąęóż]+(-[A-ZŁŹŻĆŚŃÓĘĄ][a-złźćśńąęóż])?")
        if not r.match(surname):
            return False
        return True
    
    @staticmethod
    def check_address(address):
        r = re.compile(r'^[A-ZŁŹŻĆŚŃÓĘĄ][a-złźćśńąęóż]+\s\d+(/\d+)?$')
        if not r.match(address):
            return False
        return True
    
    @staticmethod
    def check_zip_code(zip_code):
        r = re.compile(r'^\d{2}-\d{3}$')
        if not r.match(zip_code):
            return False
        return True
    
    def __init__(self, name, surname, address, zip_code):
        if Order.check_name(name):
            self.name = name
        else:
            print(f"Niepoprawne imię: {name}")

        if Order.check_surname(surname):
            self.surname = surname
        else:
            print(f"Niepoprawne nazwisko: {surname}")

        if Order.check_address(address):
            self.address = address
        else:
            print(f"Niepoprawny adres: {address}")

        if Order.check_zip_code(zip_code):
            self.zip_code = zip_code
        else:
            print(f"Niepoprawny kod pocztowy: {zip_code}")

if __name__ == "__main__":
    # Testowanie poprawnych danych
    print("--- Test poprawnych danych ---")
    order1 = Order("Adam", "Kowalski", "Puławska 12/3", "12-345")
    print(f"Order 1: {order1.name} {order1.surname}, {order1.address}, {order1.zip_code}")

    order2 = Order("Zofia", "Nowak-Kowalska", "Warszawska 45", "00-950")
    print(f"Order 2: {order2.name} {order2.surname}, {order2.address}, {order2.zip_code}")

    
    print("-"*33)
    print("--- Test niepoprawnych danych ---")
    # Niepoprawne imię (mała litera)
    order3 = Order("tomek", "Nowak", "Ptasia 15", "12-345")
    
    # Niepoprawne nazwisko (mała litera i niepoprawny separator)
    order4 = Order("Anna", "kowalska/nowak", "Długa 10/2", "12-345")
    
    # Niepoprawny adres (mała litera, brak spacji, niepoprawny format)
    order5 = Order("Jan", "Kowalski", "prosta12/", "12-345")
    
    # Niepoprawny kod pocztowy
    order6 = Order("Maria", "Wiśniewska", "Krótka 5", "1-23-45")
    
    # Test z wszystkimi błędnymi danymi
    order7 = Order("jan", "kowalski", "krótka5", "12345")
