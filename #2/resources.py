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

def sort_tuple(input_tuple: tuple[int, ...]) -> list[int]:
    x = list(input_tuple)
    return sorted(x)


def calc_empty_fields(array: list[list[int | None]]) -> int:
    empty_count = 0
    for col in array:
        for element in col:
            if element is None:
                empty_count += 1
    return empty_count