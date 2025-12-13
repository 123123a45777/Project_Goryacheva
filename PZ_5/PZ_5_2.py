def Minmax(X, Y):
    if X > Y:
        X, Y = Y, X
    return X, Y


try:
    A = float(input("A = "))
    B = float(input("B = "))
    C = float(input("C = "))
    D = float(input("D = "))

    # 4 вызова Minmax как в условии
    A, B = Minmax(A, B)  # теперь A <= B
    C, D = Minmax(C, D)  # теперь C <= D
    A, C = Minmax(A, C)  # минимальное в A
    B, D = Minmax(B, D)  # максимальное в D

    print(f"Минимальное: {A}")
    print(f"Максимальное: {D}")
except ValueError as e:
    print(e)