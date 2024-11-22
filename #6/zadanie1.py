from abc import ABC, abstractmethod

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
    calculate_discount()
        Calculates discounted price
    display_info()
        Shows product information
    __sub__(amount)
        Decreases stock quantity
    __add__(amount)
        Increases stock quantity
    """
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def calculate_discount(self):
        """
        Calculates the discounted price.
        """
        pass

    def display_info(self):
        """
        Displays information about product.
        """
        print(f"Product: {self.name}, Price: {round(self.price, 2)}PLN, Amount: {self.stock}")

    def __sub__(self, amount):
        """
        Removes items from stock.

        Parameters
            amount(int): Quantity to remove

        Returns
            Product: Reference to self
        """
        if self.stock < amount:
            print('This operation cannot be perfom.')
        else:
            self.stock -= amount
            return self

    def __add__(self, amount):
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
    calculate_discount():
        Overrides the abstract method of the parent class, returns the price of the product after the discount
    display_info():
        Overrides the parent class method, displays product information
    """
    def __init__(self,name,price,stock,author,genre,pages):
        Product.__init__(self,name,price,stock)
        self.author = author
        self.genre = genre
        self.pages = pages
    
    def calculate_discount(self):
        return 0.9 * self.price

    def display_info(self):
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
    calculate_discount():
        Overrides the abstract method of the parent class, returns the price of the product after the discount
    display_info():
        Overrides the parent class method, displays product information
    """
    def __init__(self,name,price,stock,brand,warranty,power):
        Product.__init__(self,name,price,stock)
        self.brand = brand
        self.warranty = warranty
        self.power = power
    
    def calculate_discount(self):
        return 0.95 * self.price

    def display_info(self):
        Product.display_info(self)
        print(f"Device brand: {self.brand}, Warranty {self.warranty}, Power: {self.power}W, 5% Discount: {round(self.calculate_discount(), 2)}PLN")

def check_all_products(order):
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

    order_list = {book: 2, device: 1}
    check_all_products(order_list)
    print('-'*10)

    print(f"Number of books: {book.stock}")
    book -= 1
    print(f"Number of books(removed 1): {book.stock}")
    book += 4
    print(f"Number of books(added 4): {book.stock}")
    print('-'*10)

    check_all_products(order_list)
    print('-'*10)
    print('And one more test, try to remove 30 books:')
    book -= 30