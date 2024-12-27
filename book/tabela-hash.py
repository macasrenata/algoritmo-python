# TABELA HASH 

# uma função hash é uma função onde vc insere uma string e depois disso a função retorna um numero

# tecnicamente a função hash mapeia strings e numeros

# os requisitos para a função hash é que 1. ela deve ser consistente. 2. ela deve mapear diferentes palavras para diferentes numeros

# ou seja, uma função hashnmapeia strings e as relaciona a numeros

# função hash informa a posição exata de um elemento em uma tabela. E isso funciona pq:

# 1. a função hash mapeia consistetemente um nome para o mesmo indice
# 2. a função hash mapeia diferentes strings para diferentes indices
# 3. a função hash tem conhecimento do tamanho da tabela ou array, e retornara apenas indices validos

# exemplo:

# hash('abacate') = 3
# hash('banana') = 5
# hash('cachorro') = 7

def hash(s):
    h = 0
    for c in s:
        h = h + ord(c)
    return h % 10

print(hash('abacate'))

# tabela hash é uma estrutura de dados que implementa uma função hash