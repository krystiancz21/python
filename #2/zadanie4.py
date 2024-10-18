from resources import sort_tuple, calc_empty_fields, calculated_statistics

# Zadanie 1
print("--- Zadanie 1 ---")
example_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_avg, result_median = calculated_statistics(example_numbers)
print(f"Średnia 1: {result_avg}")
print(f"Mediana 1: {result_median}")

# Zadanie 2
print("--- Zadanie 2 ---")
example_tuple = (5, 2, 8, 1, 9, 3, 7)
sorted_list = sort_tuple(example_tuple)
print(f"Oryginalna krotka 1: {example_tuple}")
print(f"Posortowana lista 1: {sorted_list}")

# Zadanie 3
print("--- Zadanie 3 ---")
example_array = [
    [1, None, 3],
    [None, 5, 6],
    [7, 8, None],
    [None, None, 11]
]

empty_count = calc_empty_fields(example_array)
print(f"Liczba pustych pól w tablicy 1: {empty_count}")