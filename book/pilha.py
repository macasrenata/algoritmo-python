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



