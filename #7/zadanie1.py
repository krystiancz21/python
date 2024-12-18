import csv
from collections import namedtuple
from exceptions import NameException, EmailException, IndexException, GradeException

Grade = namedtuple('Grade', ['subject', 'grade'])

class Student:
    students = [] 

    def __init__(self, imie: str, nazwisko: str, numer_indeksu: str, email: str, oceny: list[Grade]):
        """Inicjalizuje studenta z walidacją danych."""
        try:
            self._valid_input_data(imie, nazwisko, numer_indeksu, email, oceny)
            self.imie = imie
            self.nazwisko = nazwisko
            self.numer_indeksu = numer_indeksu
            self.email = email
            self.oceny = oceny
            self.srednia = sum(float(ocena.grade) for ocena in oceny) / len(oceny)
            Student.students.append(self)
        except (NameException, EmailException, IndexException, GradeException) as e:
            raise e

    @staticmethod
    def _valid_input_data(imie: str, nazwisko: str, numer_indeksu: str, email: str, oceny: list[Grade]) -> None:
        """Sprawdza poprawność danych studenta i zgłasza odpowiednie wyjątki."""
        if not (imie[0].isupper() and nazwisko[0].isupper()):
            raise NameException("Imię i nazwisko muszą zaczynać się wielką literą")
        
        try:
            if int(numer_indeksu) < 0:
                raise IndexException("Numer indeksu nie może być ujemny")
        except ValueError:
            raise IndexException("Nieprawidłowy format numeru indeksu")
            
        if not email.endswith("@pollub.edu.pl"):
            raise EmailException("Email musi kończyć się domeną @pollub.edu.pl")
            
        for ocena in oceny:
            if not (0 <= float(ocena.grade) <= 5):
                raise GradeException(f"Nieprawidłowa ocena z przedmiotu {ocena.subject}")

    def display_student(self):
        """Wyświetla informacje o studencie."""
        print(f"({self.numer_indeksu}) {self.imie} {self.nazwisko} - {self.email}")
        print(" - Oceny:")
        for ocena in self.oceny:
            print(f"   - {ocena.subject}: {ocena.grade:.2f}")
        print(f" - Średnia: {self.srednia:.2f}\n")

    def save_to_file(self, sciezka: str):
        """Zapisuje dane studenta do pliku CSV."""
        try:
            try:
                with open(sciezka, 'r', encoding='utf-8') as plik:
                    if not plik.readline().strip():
                        with open(sciezka, 'w', encoding='utf-8') as new_file:
                            new_file.write("Imię;Nazwisko;Numer indeksu;Email;Oceny\n")
            except FileNotFoundError:
                with open(sciezka, 'w', encoding='utf-8') as plik:
                    plik.write("Imię;Nazwisko;Numer indeksu;Email;Oceny\n")
            
            with open(sciezka, 'a', encoding='utf-8') as plik:
                dane = [self.imie, self.nazwisko, self.numer_indeksu, self.email]
                oceny_str = ';'.join([f"('{ocena.subject}',{ocena.grade})" for ocena in self.oceny])
                dane.append(oceny_str)
                plik.write(';'.join(dane) + '\n')
        except OSError as e:
            print(f"Nie można otworzyć pliku: {e}")

    @classmethod
    def read_form_file(cls, sciezka: str):
        """Wczytuje studentów z pliku CSV z nowym formatem ocen."""
        try:
            cls.students.clear()
            with open(sciezka, 'r', encoding='utf-8') as plik:
                reader = csv.reader(plik, delimiter=';')
                next(reader)
                for wiersz in reader:
                    if len(wiersz) >= 5:
                        oceny = []
                        for ocena_str in wiersz[4:]:
                            przedmiot = ocena_str.split(',')[0].strip("('")
                            wartosc = float(ocena_str.split(',')[1].strip(')'))
                            oceny.append(Grade(przedmiot, wartosc))
                        
                        try:
                            cls(wiersz[0], wiersz[1], wiersz[2], wiersz[3], oceny)
                        except (NameException, EmailException, IndexException, GradeException) as e:
                            print(f"Błąd przy wczytywaniu studenta {wiersz[0]} {wiersz[1]}: {e}")
                            continue
                            
                print(f"Wczytano {len(cls.students)} studentów.")
        except FileNotFoundError:
            print("Nie znaleziono pliku.")
        except Exception as e:
            print(f"Błąd podczas wczytywania pliku: {e}")

def main():
    while True:
        print("\n--- MENU KARTOTEKI STUDENTÓW ---")
        print("a. Wczytanie listy studentów z pliku o rozszerzeniu csv (domyślnie: ./studenci.csv)")
        print("b. Zapisanie nowego studenta na listę")
        print("c. Wyświetlenie ocen studenta o podanym nazwisku")
        print("d. Wyświetlenie listy studentów posortowanej względem średniej ocen")
        print("e. Wyjście z programu")
        print("f. Wyświetl listę studentów")

        wybor = input("Wybierz opcję: ").lower()

        if wybor == 'a':
            file_path = input("Podaj ścieżkę dostępu do pliku: ")
            Student.read_form_file(file_path)
        elif wybor == 'b':
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            numer_indeksu = input("Podaj numer indeksu: ")
            email = input("Podaj email: ")
            
            oceny = []
            while True:
                przedmiot = input("Podaj przedmiot (lub 'koniec' aby zakończyć): ")
                if przedmiot.lower() == 'koniec':
                    break
                ocena = float(input(f"Podaj ocenę z {przedmiot}: "))
                oceny.append(Grade(przedmiot, ocena))
            
            try:
                student = Student(imie, nazwisko, numer_indeksu, email, oceny)
                student.save_to_file('studenci.csv')
                print("Student został dodany i zapisany do pliku.")
            except (NameException, EmailException, IndexException, GradeException) as e:
                print(e)
        elif wybor == 'c':
            nazwisko = input("Podaj nazwisko studenta: ")
            wyniki = [s for s in Student.students if s.nazwisko.lower() == nazwisko.lower()]
            
            if not wyniki:
                print(f"Nie znaleziono studenta o nazwisku {nazwisko}")
                continue
            
            for student in wyniki:
                student.display_student()
        elif wybor == 'd':
            if not Student.students:
                print("Brak studentów w kartotece.")
                continue
            
            sorted_students = sorted(
                Student.students,
                key=lambda s: s.srednia,
                reverse=True
            )
            
            print("\nRanking studentów według średniej ocen:")
            for i, student in enumerate(sorted_students, 1):
                print(f"{i}. {student.imie} {student.nazwisko} - średnia: {student.srednia:.2f}")
        elif wybor == 'e':
            print("Zamykanie programu...")
            break
        elif wybor == 'f':
            for student in Student.students:
                student.display_student()
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
