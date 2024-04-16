numeros = [100, 23, 0, 5, 53, 7, 70, 2, 60, 90, 3, 46, 45]

def quicksort(lista, primero, ultimo):
    """Método de ordenamiento quicksort."""
    izquierda = primero
    derecha = ultimo-1
    pivote = ultimo
    print('indices', izquierda, derecha, lista[pivote])

    while (izquierda < derecha):

        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha):
            izquierda += 1
            print('deplazamineto izquierda', lista, izquierda)
            a = input()

        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda):
            derecha -= 1
            print('deplazamineto derecha', lista, derecha)
            a = input()

        if(izquierda < derecha):
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
            print('intercambio interno', lista)
            a = input()

    if(lista[pivote] < lista[izquierda]):
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
        print('intercambio pivote', lista)
        a = input()

    print('llamdas recursivas')
    if(primero < izquierda):
        quicksort(lista, primero, izquierda-1)
    if(ultimo > izquierda):
        quicksort(lista, izquierda+1, ultimo)


quicksort(numeros, 0, len(numeros)-1)