def month_to_season(num):
    if 1 <= num <= 2 or num == 12:
        return "Зима"
    elif 3 <= num <= 5:
        return "Весна"
    elif 6 <= num <= 8:
        return "Лето"
    elif 9 <= num <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("Пожалуйста, введите целое число от 1 до 12.")
