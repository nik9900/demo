z = input("Введите выражение (например, 1 + 2): ")
def calculator(main):
    parts = main.split()
    if len(parts) != 3:
        return "Ошибка: неправильный формат."
    a, operator, b = parts
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        return "Ошибка: оба значения должны быть целыми числами."
    if not (1 <= a <= 10) or not (1 <= b <= 10):
        return "Ошибка. Числа должны быть в диапазоне от 1 до 10."
    if operator == '+':
        return a + b
    elif operator == '-':
        return  a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return "Ошибка: деление на ноль."
        return a // b
    else:
        return "Ошибка: неизвестный оператор."
s = calculator(z)
print(s)
