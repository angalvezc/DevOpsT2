def permutaciones(lista):
    if len(lista) == 0:
        return [[]]
    resultado = []
    for i in range(len(lista)):
        elem = lista[i]
        resto = lista[:i] + lista[i+1:]
        for p in permutaciones(resto):
            resultado.append([elem] + p)
    return resultado

# Ejemplo de uso
lista = [1, 2, 3]
for p in permutaciones(lista):
    print(p)