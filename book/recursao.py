# recursão
# é uma técnica de programação onde uma função chama a si mesma
# caso base e caso recursivo

# dividir para conquistar

# Recursão pode ser feita com um loop - while até finalizar (arrumando em pilhas)
# ou com recursão de cauda - a chamada recursiva é a última instrução da função

# Ou seja, recursão é quando a função chama a si mesma

# pseudocodigo:

def procure_chave(caixa):
    for item in caixa:
        if item.is_a_box():
            procure_chave(item)
        elif item.is_a_key():
            print("Achei a chave!")

# A função procure_chave() é recursiva, pois chama a si mesma

# Recursão é usada para deixar a resposta mais clara e mais simples

# " Os loops podem melhorar o desempenho do seu programa. A recursão melhora o desempenho do programador. Escolha o que for mais importante para a sua situação. " - Leigh Caldwell

# é preciso cuidar para que a função recursiva não termine num loop infinito

# exemplo: quero uma contagem regressiva: 3,2,1 ...

# podemos escrever de forma recursiva:

def regressiva(i):
    print(i)
    regressiva(i - 1)

# o loop recursivo sera infinito, pois não temos um caso base

# para resolver isso, precisamos de um caso base, ou seja, informar quando a função deve parar

# caso recursivo é quando a função chama a si mesma

# caso base é quando a função não chama a si mesma

# exemplo: contagem regressiva com caso base

def regressiva(i):
    print(i)
    if i <= 1:
        return
    else:
        regressiva(i - 1)

# a função regressiva() chama a si mesma com i - 1, até que i seja menor ou igual a 1

