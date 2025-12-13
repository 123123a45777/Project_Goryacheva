def main(n):
    steps = 0
    while n > 0:
        digit_sum = sum(int(d) for d in str(n))
        n -= digit_sum
        steps += 1
    return steps

try:
    num = int(input("Введите число: "))
    if num < 0:
        print("Число должно быть неотрицательным")
    else:
        result = main(num)
        print(f"Количество действий: {result}")
except ValueError:
    print("Ошибка: введите целое число")