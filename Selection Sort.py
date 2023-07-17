def executar_selection_sort(lista):
    n = len(lista)

    for i in range(0,n):
        index_menor=i
        for j in range(i+1, n):
            if lista[j]< lista[index_menor]:
                index_menor= j
        lista[i], lista[index_menor]= lista[index_menor], lista[i]
    return lista


lista= [10,9,5,8,1,11,-1,3]
executar_selection_sort(lista)


def executar_selection_sort_2(lista):
    lista_ordenada = []
    while lista:
        minimo = min(lista)
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada


lista = [10, 9, 5, 8, 11, -1, 3]
executar_selection_sort_2(lista)