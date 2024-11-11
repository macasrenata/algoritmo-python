# Pilha de chamada (call stack)

# conceito importante para a recursão é a pilha de chamada

# A pilha de chamada é a pilha de todas as chamadas de função que estão ativas no momento

# exemplo: Lista de afazeres em papel, onde vc vai empilhar as notas uma em cima da outra, conforme vai fazendo as tarefas da lista vc remove a nota do topo da pilha

# A pilha de chamada é como uma pilha de pratos, onde vc coloca um prato em cima do outro, e remove o prato do topo da pilha

# as ações para essa pilha são duas: push(inserir) no topo da lista e pop(remover) do topo da lista

# exemplo:

def saudacao(nome):
    print("Olá, " + nome + "!")
    saudacao2(nome)
    print("Preparando para dizer tchau...")
    tchau(nome)

# então essa função chama saudacao2() e tchau()

def saudacao2(nome):
    print("Como vai, " + nome + "?")

def tchau(nome):
    print("Tchau, " + nome + "!")

# quando chamamos saudacao("Alice"), a pilha de chamada fica assim:

# 1. saudacao("Alice")
# 2. saudacao2("Alice")
# 3. tchau("Alice")

# a pilha de chamada é uma pilha de chamadas de função

# quando vc chama uma função a partir de outra, a chamada de função fica pausada em um estado parcialmente completo

# os valores das variaveis daquela função ainda ficam armazenados na memória

# essa pilha usada para guardar as variaveis de multiplas funções é denominada pilha de chamada

## PILHA DE CHAMADA COM RECURSÃO

#FUNÇÕES RECURSIVAS TAMBÉM PODEM USAR PILHA DE CHAMADA

# exemplo fat(fatorial).fat(5) = 5*4*3*2*1 = 120

# fat(3) = 3*2*1 = 6

# abaixo temos uma função recursiva para calcular o fatorial de um numero

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)  # a função chama a si mesma (recursividade )
    
print(fat(3))

# recapitulando:

# recursão é quando uma função chama a si mesma
# toda função recursiva tem o caso base, que é a condição que faz a função parar de chamar a si mesma e caso recursivo, que é a condição que faz a função chamar a si mesma
# uma pilha tem duas operações principais: push e pop
# todas as chamadas de função vão para a pilha de chamada
# a pilha de chamada pode ficar muito grande, o que pode consumir muita memória, para este caso é melhor usar um loop




