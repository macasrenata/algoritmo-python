# Quicksort = dividir para conquistar

# O algoritmo Quicksort é um algoritmo de ordenação eficiente e também é um exemplo de algoritmo de dividir para conquistar. 
# Ele escolhe um elemento como pivô e particiona o array de forma que os elementos menores que o pivô fiquem de um lado e os maiores do outro. 
# Os elementos iguais ao pivô podem ficar em qualquer lado. Em seguida, ele ordena recursivamente os subarrays.


# Quicksort é um algoritimo de ordenação muito mais rapido que o algoritimo de ordenação de seleção e de bolha

# Os algoritimos de dividir para conquistar são recursivos!

# E para resolver problema, é necessario seguir 2 passos:

# 1. Descubra o caso base, que deve ser o caso mais simples possivel
# 2. Divida e diminua o seu problema até que ele se torne o caso base


# esse algoritmo não é um simples algoritmo que você aplica em varios problemas, mas uma maneira de pensar sobre o problema



# exemplo:

# vc tem um array : [ 2, 4, 6]
# vc deve somar todos os numeros e retornar o valor total, isto é simples de fazer com o loop

def sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum([2, 4, 6]))

# mas e se vc quiser fazer de maneira recursiva?

# vc deve seguir os passos:

# 1. Descubra o caso base, que deve ser o caso mais simples possivel
# 2. Divida e diminua o seu problema até que ele se torne o caso base

# caso base: se o array for vazio, o total é 0
# caso recursivo: o total é o primeiro elemento do array mais a soma do restante do array

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print(sum([2, 4, 6]))

# ou seja:

# 1. Pegue uma lista
# 2. Se a lista estiver vazia, retorne 0
# 3. Caso contrário, some o primeiro elemento com a soma do restante da lista

# o caso sem o loop é programação funcional, e é mais dificil de entender, mas é mais poderoso, pois tem linguagens que são feitas para isso, como Haskell, Scala, Clojure, etc

# exercicios:

# 1. escreva o código para a função soma, vista anteriormente:

def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

print(sum([2, 4, 6]))

# 2. Escreva uma função recursiva que conte o numero de itens em uma lista:

def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

print(count([2, 4, 6]))

# Encontre o valor mais alto em uma lista:

def max(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(max([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))

# 4. Voce lembra da pesquisa binaria? Ela tambem é um algoritmo de dividir e conquistar. Voce consegue determinar o caso base e o caso recursivo para a pesquisa binaria?

# é um array com 1 item, se vc esta procurando combinar com o item presente no array, vc encontrou, caso contrario ele não esta no array
# no caso recursivo para pesquisa binaria, vc divide o array pela metade, joga fora uma metade e executa uma pesquisa binaria na outra metade


# caso base: se a lista estiver vazia, retorne False
# caso recursivo: se o primeiro elemento da lista for igual ao item, retorne True. Caso contrário, procure o item na metade da lista

def binary_search(arr, item):
    if len(arr) == 0:
        return False
    guess = arr[len(arr) // 2]
    if guess == item:
        return True
    if guess > item:
        return binary_search(arr[:len(arr) // 2], item)
    else:
        return binary_search(arr[len(arr) // 2 + 1:], item)
    
print(binary_search([1, 3, 5, 7, 9], 3))



# Quicksort

# O Quicksort é um algoritmo de ordenação muito mais rapido que o algoritimo de ordenação de seleção e de bolha
# O  algoritmo Quicksort também utiliza a técnica de dividir para conquistar, mas ele não divide o array em subarrays de tamanhos iguais.

# alguns arrays não precisam ser ordenados, quando ele esta vazio ou com um elemento

# caso base: se o array tiver menos de 2 elementos, retorne o array

# caso recursivo: escolha um elemento do array e divida o array em 2 subarrays

def quicksort(array):
    if len(array) < 2:
        return array
    
# um array com 2 elementos é simples de ordenar, basta verificar se o primeiro elemento é maior que o segundo e trocar de lugar se for o caso

# caso base: se o array tiver 2 elementos, retorne o array ordenado

# caso recursivo: escolha um elemento do array e divida o array em 2 subarrays

def quicksort2(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort2(less) + [pivot] + quicksort2(greater)
    
print(quicksort2([10, 5, 2, 3]))

# um array com 3 elementos é um pouco mais complicado, mas ainda é facil de ordenar

# escolhemos elemento do array que chamamos de pivô (primeiro item do array)
# encontramos os elementos que são menores do que o pivô e os que são maiores
# isso é chamado de particionamento

# - então vc tem um subarray com os elementos menores do que o pivô
# - pivô
# - um subarray com os elementos maiores do que o pivô

# os dois subarrays não estão ordenados, mas vc pode ordena-los facilmente com o quicksort

# se vc ordenar os subarrays e juntar tudo, vc terá um array ordenado

# os passos para ordenar um array de 3 elementos são:

# 1. Escolha um elemento do array e chame-o de pivô
# 2. Divida os elementos restantes em 2 subarrays: elementos menores do que o pivô e elementos maiores do que o pivô
# 3. Ordene os subarrays e junte-os, ou seja execute o quicksort nos subarrays recursivamente

# Notação BigO revisada:

# quicksort é unico, pois sua velocidade depende da escolha do pivô

# tempo de execução de big0 para quicksort é O(n log n)


