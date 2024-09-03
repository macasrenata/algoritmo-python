# pesquisa binaria 

# entrada é uma lista ordenada de elementos se o elemento que esta buscando esta na lista ele retorna o valor do indice do elemento caso contrario retorna -1[none]

# pesquisa binaria para uma lista de n numeros precisa de log2n passos para encontrar o valor

# baixo = 0
# alto = len(lista) -1

# meio = (baixo + alto) // 2

# chute = lista[meio]

# if chute < item:
#     baixo = meio + 1

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 3)) # => 1
print(pesquisa_binaria(minha_lista, -1)) # => None


# O(n) - complexidade linear -- percorre todos os elementos da lista
# O(log n) - complexidade logaritmica -- pesquisa binaria - começa do meio da lista e vai dividindo pela metade
