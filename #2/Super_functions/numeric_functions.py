# obliczająca sumę cyfr w liczbie
def sum_of_digits(input_number: int) -> int:
    sum = 0
    for digit in str(abs(input_number)):
        sum += int(digit)
    return sum

# obliczająca silnię liczby
def calc_factorial(n: int) -> int:
    if n < 0:
        print("Silnia nie jest zdefiniowana dla liczb ujemnych.")
        return None;
    if n == 0 or n == 1:
        return 1
    return n * calc_factorial(n - 1)