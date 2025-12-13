# 2. Дан список размера N. Найти количество его промежутков монотонности
#    (то есть участков, на которых его элементы возрастают или убывают).

try:
    N = int(input("N = "))
    A = [int(input(f"A[{i}] = ")) for i in range(N)]

    if N < 2:
        count = 1 if N == 1 else 0
    else:
        count = 1
        direction = 0  # 0 - не определено, 1 - возрастает, -1 - убывает

        for i in range(1, N):
            if A[i] > A[i - 1]:
                if direction == -1:
                    count += 1
                direction = 1
            elif A[i] < A[i - 1]:
                if direction == 1:
                    count += 1
                direction = -1

    print(f"Количество промежутков монотонности: {count}")
except ValueError:
    print("Ошибка ввода")