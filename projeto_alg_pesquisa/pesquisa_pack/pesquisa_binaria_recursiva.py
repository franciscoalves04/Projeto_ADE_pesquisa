def pesquisa_binaria_recursiva(lista, item):
    if len(lista) == 0:
        return False
    else:
        meio = len(lista) // 2
        if lista[meio] == item:
            return True
        else:
            if item < lista[meio]:
                return pesquisa_binaria_recursiva(lista[:meio], item)
            else:
                return pesquisa_binaria_recursiva(lista[meio + 1:], item)
