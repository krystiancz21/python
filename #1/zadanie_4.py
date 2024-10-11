from datetime import datetime

now = datetime.now()

print(f"Data i czas teraz: {now}")

day_start = datetime(now.year, now.month, now.day, 00, 0, 0)
day_end = datetime(now.year, now.month, now.day, 23, 59, 59)
day_passed = (now - day_start).total_seconds()
day_last = (day_end - day_start).total_seconds()

day_percent = (day_passed / day_last) * 100

print(f"Procent dnia, który minął: {day_percent:.2f}%")


# --- Wstęp do lab ---
# now = datetime.now()

# print(f"Data i czas teraz: {now}")
# print(f"Data i czas dzisiaj: {now.day}")

# past = datatime(now.year-2, now.month+1, now.day+12, 12, 15, 25)
# print(f"DAta i czas kiedys: {past}")

# diff = now - past 
# print(f"Rożnica: {diff}")
# print(f"Rożnica w sekundach: {diff}")