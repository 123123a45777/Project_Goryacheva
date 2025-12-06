"""Вариант 10.
1. Дано целое число N (> 0). Найти сумму N^2 + (N + 1)^2? + (N + 2)^2? + ... + (2N)^2"""
try:
    N = int(input("Введите N (>0): "))

    total = 0
    k = N
    while k <= 2 * N:
        total += k * k
        k += 1

    print(total)
except ValueError as e:
    print(e)