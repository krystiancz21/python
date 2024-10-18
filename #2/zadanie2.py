def sort_tuple(input_tuple: tuple[int, ...]) -> list[int]:
    x = list(input_tuple)
    return sorted(x)

# Zadanie 2
example_tuple = (5, 2, 8, 1, 9, 3, 7)
sorted_list = sort_tuple(example_tuple)
print(f"Oryginalna krotka 1: {example_tuple}")
print(f"Posortowana lista 1: {sorted_list}")

example_tuple2 = (5, 1, 9, 3, 5, 6, 5, 7, 7)
sorted_list2 = sort_tuple(example_tuple2)
print(f"Oryginalna krotka 2: {example_tuple2}")
print(f"Posortowana lista 2: {sorted_list2}")