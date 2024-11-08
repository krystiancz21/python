def median_or_average(*args):
    """
    Funkcja przyjmuje dowolną listę argumentów i w zależności od ich typu wykona odpowiednie operacje.
        - jeśli *args to liczby - zwróci ich średnią
        - jeśli *args to napisy - zwróci medianę ich długości
        - jeśli *args to wartości mieszane, lub innego typu - wyświetli odpowiedni komunikat
    Parameters:
        *args: Dowolna liczba argumentów

    Returns:
        float: średnia liczb, mediana długości wyrazów
        str: komunikat dotyczący złego typu
    """

    if all(type(x) in (int, float) for x in args):
        numbers = [float(value) for value in args]
        avg = sum(numbers) / len(numbers)
        return avg
    elif all(type(x) is str for x in args):
        items_length = [len(value) for value in args]
        sort_len = sorted(items_length)
        temp = len(sort_len) // 2
        if len(sort_len) % 2 == 0:
            return (sort_len[temp - 1] + sort_len[temp]) / 2
        else:
            return sort_len[temp]
    else:
        return "Incorrect types of variables"


if __name__ == "__main__":
    print(f"Wynik dla typu int: {median_or_average(1, 2, 6)}")
    print(f"Wynik dla typu float: {median_or_average(1.5, 2.25, 6.6)}")
    print(f"Wynik dla int + float: {median_or_average(1, 2.25, 6)}")
    print(f"Wynik da typu string: {median_or_average("raz", "dwa", "trzy", "cztery")}")
    print(f"Wynik dla różnych typów: {median_or_average(1.7, 2, "cosik")}")
