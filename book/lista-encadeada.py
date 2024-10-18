# listas encadeadas são ótimas se vc quiser ler todos os itens da lista, mas não são boas para pesquisas

# Arrays são diferentes, pois vc sabe o endreço de memória de cada item, então vc pode acessar qualquer item da lista em tempo constante

# a posição de um elemento em um array é chamado de índice

# [12, 15,17,20] = o numero 15 esta no indice 1


####      | Arrays    | Listas
# Leitura | O(1)      | O(n)
# Inserção| O(n)      | O(1)
# Deletar | O(n)      | O(1)

# O(n) = tempo de execução linear
# O(1) = tempo de execução constante

# Leitura:
# arrays são melhores para leitura de itens

# Inserir elementos :
# listas encadeadas são melhores de inserir elementos no meio da lista

# Deletar elementos:
# listas encadeadas são melhores para deletar elementos no meio da lista


#Existe 2 tipos de acesso: Aleatório e sequencial

# Aleatório: vc pode acessar qualquer item da lista em tempo constante
# Sequencial: vc precisa percorrer todos os itens da lista para encontrar o item que vc procura

# listas encadeadas só podem lidar com acesso sequencial
# arrays podem lidar com acesso aleatório e sequencial