def decimalforbi(n):
    pilha = []

    while n > 0:
        resto = n % 2
        pilha.append(resto)
        numero //=2

    if not pilha:
        pilha.append (0)

    binario = ""
    while len(pilha)>0:
        binario += str(pilha.pop())

    return binario


numerodec = int(input("Escreva um numero decimal: "))
numerobi = decimalforbi(numerodec)
print(f"Número decimal {numerodec} em binário é: {numerobi}")