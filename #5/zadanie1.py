class Book:
    """
    A class representing a book.

    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    year (int): The publication year of the book.
    genre (str): The genre of the book.
    """
    def __init__(self, title: str, author: str, year: int, genre: str) -> None:
        """
        Initializes a new instance of the Book class.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
            genre (str): The genre of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre


if __name__ == "__main__":
    book1: Book = Book("Lalka", "B. Prus", 1889, "Powieść")
    book2: Book = Book("Stary człowiek i morze", "E. Hemingway", 1952, "Opowiadanie")
    book3: Book = Book("Krzyżacy", "H. Sienkiewicz", 1900, "Powieść historyczna")
    print(f"Tytuł: {book1.title}, Autor: {book1.author}, Rok: {book1.year}, Gatunek: {book1.genre}")
    print(f"Tytuł: {book2.title}, Autor: {book2.author}, Rok: {book2.year}, Gatunek: {book2.genre}")
    print(f"Tytuł: {book3.title}, Autor: {book3.author}, Rok: {book3.year}, Gatunek: {book3.genre}")
