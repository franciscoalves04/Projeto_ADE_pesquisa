def pesquisa_sequencial(lista, objeto):
    for i in range(len(lista)):
        if lista[i] == objeto:
            return i
    return "Não existe"

t = pesquisa_sequencial([1,2,3,4,4], 8)
print(t)
