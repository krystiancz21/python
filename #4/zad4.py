def print_data_or_save_to_file(*args, **kwargs):
    """
    Funkcja przyjmująca dowolną liczbę argumentów i wykonująca operacje na nich.
    Parameters:
        *args: Argumenty, które przekazane są przez pozycję
        **kwargs: Argumenty, które przekazane są przez nazwę

    Returns:
        None: Wyniki są wyświetlane na konsoli lub zapisywane do pliku.
    """

    if args and not kwargs:
        output_result = list(args)
        print("\t".join(map(str, output_result)))
    elif kwargs and not args:
        with open("zad4.txt", "w") as file:
            for key, value in kwargs.items():
                file.write(f"{key} -> {value}\n")
    elif kwargs and args:
        output_result = dict(enumerate(args))
        output_result.update(kwargs)
        for key, value in output_result.items():
            print(f"{key} -> {value}")


if __name__ == "__main__":
    print("Argumenty przekazane przez pozycję:")
    print_data_or_save_to_file(1, 2, 3, 4)

    print("Argumenty przekazane przez nazwę - wynik w pliku zad4.txt")
    print_data_or_save_to_file(hello="world", pollub="student")

    print("Argumenty różne:")
    print_data_or_save_to_file("Ben", 10, 2.0, three="trzy[3]")
