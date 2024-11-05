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

