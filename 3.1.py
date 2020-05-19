def division():
    a = float(input("Введите числитель: "))
    b = float(input("Введите знаменатель: "))
    try:
        answer = a / b
    except ZeroDivisionError:
        print("Деление на ноль!")
    return answer

print(division())
