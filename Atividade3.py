def inver(string):
    pilha = []
    for char in string:
        pilha.append(char)

    stringinvertida = ""
    while len(pilha)> 0:
        stringinvertida += pilha.pop()

    return stringinvertida

texto = input("texto: ")
textoinv = inver(texto)
print ("Texto invertido: ", textoinv)