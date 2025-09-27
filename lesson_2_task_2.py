def is_year_leap(namber):
    if namber % 4 == 0:
        return True
    elif namber >= 1:
        return False


namber = int(input("Введите год: "))
result = is_year_leap(namber)
print(f"Год {namber}: {result} ")
