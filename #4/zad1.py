def sort_by_number_of_digits(input_list):
    """
    Sortuje listę liczb całkowitych względem liczby cyfr.
    Parametrs:
        input_list (list): Lista zawierająca liczby całkowite do posortowania
    
    Returns:
        list: Zwraca posortowaną listę liczb względem ilości cyfr
    """
    sort_list = lambda x: len(str(abs(x)))
    return sorted(input_list, key=sort_list)

def find_min_value(input_list):
    """
    Znajduje liczbę o najmniejszej liczbie cyfr w liście.
    Parameters:
        input_list (list): Lista zawierająca liczby całkowite
    
    Returns:
        int: Liczba o najmniejszej liczbie cyfr
    """
    sort_list = lambda x: len(str(abs(x)))
    return min(input_list, key=sort_list)

def find_max_value(input_list):
    """
    Znajduje liczbę o największej liczbie cyfr w liście.
    Parameters:
        input_list (list): Lista zawierająca liczby całkowite
    
    Returns:
        int: Liczba o największej liczbie cyfr
    """
    sort_list = lambda x: len(str(abs(x)))
    return max(input_list, key=sort_list)


if __name__ == "__main__":
    liczby = [543, 34523, 3, 23, 5432345, 234]
    print(f"Lista wejściowa: {liczby}")
    print(f"Lista posortowana po liczbie cyfr: {sort_by_number_of_digits(liczby)}")
    print(f"Liczba o najmniejszej liczbie cyfr: {find_min_value(liczby)}")
    print(f"Liczba o największej liczbie cyfr: {find_max_value(liczby)}")