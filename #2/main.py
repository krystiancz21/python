from Super_functions import (
    sum_of_digits,
    calc_factorial,
    words_in_string,
    reverse_words_in_string,
    remove_whitespace,
)
if __name__ == "__main__":
    print("Funkcje numeryczne:")
    print(f"Suma cyfr liczby 123: {sum_of_digits(123)}")
    print(f"Suma cyfr liczby 335: {sum_of_digits(-335)}")
    print(f"Suma cyfr liczby 21212: {sum_of_digits(21212)}")
    print("---")
    print(f"Silnia z 5: {calc_factorial(5)}")
    print(f"Silnia z 8: {calc_factorial(8)}")
    print(f"Silnia z -2: {calc_factorial(-2)}")
    print("---")

    print("Funkcje operujące na napisach:")
    test_text = "  To tekst zakopane na pokaz  "
    print(f"Oryginalny tekst: '{test_text}'")
    print("---")
    print(f"Liczba wyrazów: {words_in_string(test_text)}")
    print("---")
    print(f"Odwrócona kolejność wyrazów: '{reverse_words_in_string(test_text)}'")
    print("---")
    print(f"Tekst bez białych znaków: '{remove_whitespace(test_text)}'")
