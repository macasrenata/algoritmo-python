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

