from abc import ABC, abstractmethod

# Zadanie 1
class Product(ABC):
    """
    Abstract base class for products.

    Attributes
    ----------
    name : str
        Product name
    price : float
        Product price
    stock : int
        Available quantity in stock

    Methods
    -------
    calculate_discount() -> float:
        Calculates the discounted price for the product
    display_info() -> None:
        Shows product information
    __sub__(amount: int) -> Product:
        Decreases stock quantity by the specified amount
    __add__(amount: int) -> Product:
        Increases stock quantity by the specified amount
    """
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def calculate_discount(self) -> float:
        """
        Calculates the discounted price.
        """
        pass

    def display_info(self)-> None:
        """
        Displays information about product.
        """
        print(f"Product: {self.name}, Price: {round(self.price, 2)}PLN, Amount: {self.stock}")

    # Zadanie 3. przeciążenia operatorów sub i add
    def __sub__(self, amount: int):
        """
        Removes items from stock.

        Parameters
            amount(int): Quantity to remove

        Returns
            Product: Reference to self
        """
        if self.stock < amount:
            print('This operation cannot be perfom!')
        else:
            self.stock -= amount
            return self

    def __add__(self, amount: int):
        """
        Adds items to stock.

        Parameters
            amount(int): Quantity to add

        Returns
            Product: Reference to self
        """
        self.stock += amount
        return self
    

class Book(Product):
    """
    Class representing a book.

    Attributes
    ----------
    author : str
        Book author
    genre : str
        Book genre
    pages : int
        Number of pages
    
    Methods
    -------
    calculate_discount() -> float:
        Overrides the abstract method of the parent class, returns the price of the product after the discount
    display_info() -> None:
        Overrides the parent class method, displays product information
    """
    def __init__(self,name,price,stock,author,genre,pages):
        Product.__init__(self,name,price,stock)
        self.author = author
        self.genre = genre
        self.pages = pages
    
    def calculate_discount(self) -> float:
        return 0.9 * self.price

    def display_info(self)-> None:
        Product.display_info(self)
        print(f"Book author: {self.author}, Genre {self.genre}, Pages: {self.pages}, 10% Discount: {round(self.calculate_discount(), 2)}PLN")


class ElectronicDevice(Product):
    """
    Class representing an electronic device.

    Attributes
    ----------
    brand : str
        Device brand
    warranty : int
        Warranty period in years
    power : float
        Power consumption in watts

    Methods
    -------
    calculate_discount() -> float:
        Overrides the abstract method of the parent class, returns the price of the product after the discount
    display_info() -> None:
        Overrides the parent class method, displays product information
    """
    def __init__(self,name,price,stock,brand,warranty,power):
        Product.__init__(self,name,price,stock)
        self.brand = brand
        self.warranty = warranty
        self.power = power
    
    def calculate_discount(self) -> float:
        return 0.95 * self.price

    def display_info(self) -> None:
        Product.display_info(self)
        print(f"Device brand: {self.brand}, Warranty {self.warranty}, Power: {self.power}W, 5% Discount: {round(self.calculate_discount(), 2)}PLN")


# Funkcja do zadania 2.
def check_all_products(order: dict) -> None:
    """
    Checks product availability and saves order details to a file.

    Parameters
        order(dict): Dictionary with products and their quantities

    Creates 'orders.txt' file with order details and total price.
    Prints whether the order can be completed.
    """
    in_stock = True
    total = 0
    file = open("orders.txt", "w")

    file.write("Order details: [ - product: quantity]\n")

    for item in order:
        order_quantity = order[item]
        if order_quantity <= item.stock:
            total += order_quantity * item.price
            file.write(f" - {item.name}: {order_quantity} \n")
        else:
            file.write(f" - {item.name} is not available\n")
            in_stock = False

    file.write(f"\nTotal price: {total}PLN\n")

    if in_stock:
        print("Order can be completed.")
    else:
        print("Order cannot be completed.")
    print("Check orders.txt file, to check details.")


if __name__ == "__main__":
    book = Book("Lalka", 25.65, 1, "B. Prus", "Powieść", 255)
    book.display_info()
    print('-'*10)

    device = ElectronicDevice("Smartphone", 1550, 20, "Motorola", 5, 5.5)
    device.display_info()
    print('-'*10)

    print("Failed order:")
    failed_order = {book: 2, device: 1}
    check_all_products(failed_order)
    print('-'*10)

    print("Successful order:")
    successful_order = {book: 1, device: 1}
    check_all_products(successful_order)
    print('-'*10)

    print(f"Number of books: {book.stock}")
    book -= 1
    print(f"Number of books(removed 1): {book.stock}")
    book += 4
    print(f"Number of books(added 4): {book.stock}")
    print('-'*10)

    print('And one more test, try to remove 30 books(expecteed error):')
    book -= 30
