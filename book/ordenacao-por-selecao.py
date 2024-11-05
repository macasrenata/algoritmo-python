# arrays e listas encadeadas 

# listas encadeadas resolvem o problema de adição d eitens no meio da lista, pois não é necessario mover todos os itens para adicionar um novo item
# os itens podem estar em qualquer lugar da memoria

#arrays 
# função para encontrar o menor elemento do array

def findSmallest(arr):
    # armazena o menor valor
    smallest = arr[0]
    # armazena o indice do menor valor
    smallest_index = 0
    for i in range(1, len(arr)): # percorre o array
        if arr[i] < smallest: # se o elemento atual for menor que o menor elemento
            smallest = arr[i] # atualiza o menor elemento
            smallest_index = i # atualiza o indice do menor elemento
    return smallest_index # retorna o indice do menor elemento

# função para ordenar um array
def selectionSort(arr):
    newArr = [] # cria um novo array
    for i in range(len(arr)): # percorre o array
        # encontra o menor elemento do array e adiciona ao novo array
        smallest = findSmallest(arr) # encontra o menor elemento do array
        newArr.append(arr.pop(smallest)) # remove o menor elemento do array e adiciona ao novo array
    return newArr # retorna o novo array

print(selectionSort([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]

