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

class Library:
    """
    A class representing a library.

    Atributes:
    total_books (int): The total number of books in the library.
    books (list): A list of the Book instances.
    """
    total_books: int = 0

    def __init__(self) -> None:
        """
        Initializes a new instance of the Library class.
        """
        self.books = []
    
    def add_book(self, book: Book) -> None:
        """
        Adds a book to the library and update total_books counter value.
        
        Args:
            book (Book): An instance of the Book class. 
        """
        self.books.append(book)
        Library.total_books += 1


if __name__ == "__main__":
    my_library: Library = Library()
    book1: Book = Book("Lalka", "B. Prus", 1889, "Powieść")
    book2: Book = Book("Stary człowiek i morze", "E. Hemingway", 1952, "Opowiadanie")
    book3: Book = Book("Krzyżacy", "H. Sienkiewicz", 1900, "Powieść historyczna")
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    for index, item in enumerate(my_library.books, start=1):
        print(f"[{index}] {item.title} ({item.year}) {item.author}")

    print(f"\nLiczba książek w bibliotece: {Library.total_books} ")