import random
from collections import Counter

def random_grades(min_value=2, max_value=5, item_count=15):
    list_grades = []
    for _ in range(item_count):
        list_grades.append(random.randint(min_value, max_value))
    return list_grades

def number_of_appearances(input_items):
    return Counter(input_items)

def most_common_items(input_items, n):
    return input_items.most_common(n)

def positive_grades(grades):
    sum_positive = 0
    for grade in grades:
        if grade >= 3:
            sum_positive += 1
    return sum_positive

grades = random_grades()
grade_counts = number_of_appearances(grades)

print("---- #5 ----")
print(f"Wygenerowane oceny: {grades}")

print("Liczba wystąpień każdej oceny:")
for grade, count in grade_counts.items():
    print(f" > Ocena: {grade} - [{count}] wystąpień")

most_commmon_grades = most_common_items(grade_counts, 2)
print("Dwie najczęściej występujące oceny:")
for grade, count in most_commmon_grades:
    print(f" > Ocena {grade} z liczbą wystąpień: {count}")

print(f"Liczba ocen pozytywnych: {positive_grades(grades)}")
