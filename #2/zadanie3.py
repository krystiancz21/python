def calc_empty_fields(array: list[list[int | None]]) -> int:
    empty_count = 0
    for col in array:
        for element in col:
            if element is None:
                empty_count += 1
    return empty_count


# Zadanie 3
example_array = [
    [1, None, 3],
    [None, 5, 6],
    [7, 8, None],
    [None, None, 11]
]

empty_count = calc_empty_fields(example_array)
print(f"Liczba pustych pól w tablicy 1: {empty_count}")

example_array2 = [
    [None, None, 3],
    [None, 5, None],
    [7, 8, None],
    [None, None, None]
]
empty_count2 = calc_empty_fields(example_array2)
print(f"Liczba pustych pól w tablicy 2: {empty_count2}")