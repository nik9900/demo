
z = input("Введите выражение (например, 1 + 2): ")

def calculator(main):
    parts = main.split()
    if len(parts) != 3:
        print("Ошибка: неправильный формат.")
    a, operator, b = parts
    a=float(a)
    b=float(b)
    if a%1!=0 and b%1!=0:
            return print("Ошибка. Должно быть только целове число")
    if not (1 <= a <= 10) or not (1 <= b <= 10):
        return print("Ошибка. Числа должны быть в диапазоне от 1 до 10")
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            print("Деление на ноль")
            return

        return a / b
    else:
        print("Ошибка")

s = int(calculator(z));
print("Ответ:", s)
