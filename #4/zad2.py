def format_strings(input_strings):
    """
    Funkcja formatująca listę napisów, gdzie napis ma zaczyna się wielką literą i kończy kropką.
    Parameters:
        input_strings (list): Lista napisów do sformatowania
    
    Returns:
        list: Lista sformatowanych napisów
    """
    return list(map(lambda input: input[0].capitalize() + input[1:] + '.', input_strings))


if __name__ == "__main__":
    strings = ["ala ma kota", "kot ma ale", "ale ma kot"]
    print(format_strings(strings))