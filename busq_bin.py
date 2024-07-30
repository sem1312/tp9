def busqueda_binaria(lista, elemento):
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == elemento:
            return medio
        elif lista[medio] < elemento:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1
