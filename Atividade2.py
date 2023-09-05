def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial(n - 1)


n = 50 
resultado = fatorial(n)
print(f"Fatorial de {n} é {resultado}.")