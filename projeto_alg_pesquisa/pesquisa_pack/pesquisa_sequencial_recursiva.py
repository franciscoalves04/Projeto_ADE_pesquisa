def pesquisa_sequencial_recursiva(lista, n):
    if not lista:
        return False
    if lista[0] == n:
        return True
    return pesquisa_sequencial_recursiva(lista[1:], n)




t= pesquisa_sequencial_recursiva([1,2,3,4,5,5,6,7], 6)
print(t)