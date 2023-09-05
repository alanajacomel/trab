def soma(A):
    if A <= 0:
        return 0
    else:
        return A + soma(A - 1)


a = 50
resultado = soma(a)
print(f"A soma de {a} números inteiros positivos é {resultado}.")