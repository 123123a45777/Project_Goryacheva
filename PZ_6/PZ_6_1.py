try:
    #Ввод значений
    N = int(input("N = "))
    K = int(input("K (1 < K < N) = "))
    #Логика
    if not (1 < K < N):
        print("Ошибка: K должно быть между 1 и N")
    else:
        A = [int(input(f"A[{i}] = ")) for i in range(N)]
        result = [A[i] for i in range(K - 1, N, K)]
        print("Результат:", result)
except ValueError as e:
    print(e)