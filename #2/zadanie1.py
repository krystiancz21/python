def calculated_statistics(list_numbers: list[int | float]) -> tuple[float, float]:
    if not list_numbers:
        raise ValueError("Lista nie może być pusta")
    
    calc_avg = sum(list_numbers) / len(list_numbers)

    sorted_list = sorted(list_numbers)
    length = len(sorted_list)
    if length % 2 == 0:
        calc_median = (sorted_list[length // 2 - 1] + sorted_list[length // 2]) / 2
    else:
        calc_median = sorted_list[length // 2]

    return calc_avg, calc_median


# Zadanie 1
example_numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_avg, result_median = calculated_statistics(example_numbers)
print(f"Średnia 1: {result_avg}")
print(f"Mediana 1: {result_median}")

example_numbers_2: list[float] = [1.2, 2.4, 3.2, 4.5, 5, 6.7, 7.2, 8.4, 9, 10]
result_avg_2, result_median_2 = calculated_statistics(example_numbers_2)
print(f"Średnia 2: {result_avg_2}")
print(f"Mediana 2: {result_median_2}")
