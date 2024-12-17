import time

# merge sort tem sempre O(n log n) de tempo de execução

#diferente do quicksort que tem tempo de execução médio de O(n log n) e pior caso de O(n²)

# o merge sort é um algoritmo de ordenação muito mais rapido que o algoritimo de ordenação de seleção e de bolha

# o algoritmo merge sort também utiliza a técnica de dividir para conquistar, mas ele divide o array em subarrays de tamanhos iguais    

# caso base: se o array tiver menos de 2 elementos, retorne o array

# caso recursivo: divida o array em 2 subarrays e ordene cada um deles com o merge sort e depois junte os subarrays ordenados

# merge sort   x  quicksort 

# suponha que vc tenha uma função que imprime todos os itens de uma lista:

def print_items(lista):
    for item in lista:
        print(item)

print_items([1, 2, 3])

# como essa função passa por todos os itens da lista uma vez, ela tem tempo de execução O(n), onde n é o número de itens na lista

# agora mudei a função para aguardar um segundo entre cada item impresso:

def print_items(lista):
    for item in lista:
        time.sleep(1)
        print(item)

print_items([1, 2, 3])

# agora a função tem tempo de execução O(n), onde n é o número de itens na lista

# qual a mais rapida? a primeira, pois ela tem tempo de execução O(n), onde n é o número de itens na lista, porém é tambem O(n) a outra mesmo esperando 1 segundo entre cada item

# o tempo de execução de um algoritmo é uma maneira de medir quanto tempo ele le

# O(n) pode se ler assim: 


# 'x'alguma quantida de tempo, elevado a 'c' que que é uma quantidade de tempo determinada 'vezes' 'n' que é o número de itens na lista

# por vezes, a constante pode fazer a diferença, mas em geral, o que importa é o crescimento da função

# no caso de merge sort e quicksort, ambos tem tempo de execução O(n log n), mas o quicksort é mais rapido na pratica mesmo tendo o mesmo tempo de execução

# pois ele funciona no caso médio em O(n log n) e no pior caso em O(n²), já o merge sort sempre tem tempo de execução O(n log n)


# CASO MEDIO VERSUS PIOR CASO 

# o tempo de execução de um algoritmo pode variar dependendo dos dados de entrada (pivôs do quicksort)


# PIOR CASO: o tempo de execução do algoritmo é o mais lento possível para qualquer entrada de tamanho n

# exemplo: o quicksort tem tempo de execução O(n²) no pior caso, que ocorre quando o pivô é sempre o menor ou o maior item da lista

# codigo do pior caso do quicksort:

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

# o pior caso do quicksort ocorre quando o pivô é sempre o menor ou o maior item da lista

# o pior caso do merge sort é sempre O(n log n), pois ele sempre divide o array em subarrays de tamanhos iguais

#--------------------------------------------------------------------------------------------------------------------

# MELHOR CASO: o tempo de execução do algoritmo é o mais rapido possível para qualquer entrada de tamanho n

# exemplo: o quicksort tem tempo de execução O(n log n) no melhor caso, que ocorre quando o pivô divide a lista em duas metades iguais

# o melhor caso do merge sort é sempre O(n log n), pois ele sempre divide o array em subarrays de tamanhos iguais

# -------------------------------------------------------------------------------------------------------------------

# CASO MEDIO: o tempo de execução do algoritmo é o esperado para qualquer entrada de tamanho n

# EXERCICIOS:

# QUANTO TEMPO LEVBARIA, EM NOTAÇÃO BIG O PARA COMPLETAR CADA UMA DAS SEGUINTES OPERAÇÕES?

# 1. imprimir o valor de cada elemento em um array.

# O(n)

# 2. Duplicar o valor de cada elemento em um array.

# O(n)

# 3. Duplicar o valor apenas do primeiro elemento em um array.

# O(1)

# 4. Criar uma tabela de multiplicação com todos os elementos do array. Assim, caso o seu array seja [2,3,7,8,10], você primeiro multiplicara cada elemento por 2. Depois, multiplicara cada elemento por 3 e então por 7, e assim por diante.

# O(n²)


## RECAPITULANDO:

# A estratégia DC (dividir para conquistar) envolve dividir o problema em subproblemas menores e resolver esses subproblemas de forma recursiva. Se vc estiver usando DC em uma lista o caso-base sera geralmente um array vazio ou com apenas 1 elemento

# Se estiver usando quicksort, escolha um elemento aleatório como pivô. O tempo de execução do quicksort é O(n log n) no caso médio e O(n²) no pior caso

# A constante, na notação BIg O, é relevante em alguns casos. Esta é a razão pelo qual o quicksort é mais rapido que o merge sort na pratica, mesmo tendo o mesmo tempo de execução

# A constante, na notação Big O, dificilmente sera relevante na comparação entre pesquisa simples e pesquisa binaria. POis a pesquisa binaria é O(log n), que é muito mais rapido que a pesquisa simples, que é O(n)






































