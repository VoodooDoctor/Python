def division(a, b):
    try:
        answer = a / b
        return answer
    except ZeroDivisionError:
        return print("Деление на ноль!")

print(division(int(input("Введите чилитель = ")), int(input("Введите знаменатель = "))))
