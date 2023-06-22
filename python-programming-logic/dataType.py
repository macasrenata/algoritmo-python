#Tipo de dados

# string (texto)
"introdução ao worpress"

# integer (número inteiro)
10

# float (número decimal)
10.5

# boolean (verdadeiro ou falso)
True

# list (lista)
[10, 20, 30, 40, 50]

# tuple (tupla)
(10, 20, 30, 40, 50)



# Operações matemáticas

# soma
10 + 10

# subtração
10 - 5

# multiplicação
10 * 10

# divisão
10 / 2

# exponenciação
10 ** 2

# módulo
10 % 2

# divisão inteira
10 // 2


#Variaveis

#string 
nome = "introdução ao worpress"

# integer(integer, int)
duração = 85

# float (float)
preço = 10.5

# boolean (bool)
ativo = True

# list (list)
tags = ["wordpress", "cms", "php"]

# tuple (tuple)
tags = ("wordpress", "cms", "php")

# dictionary (dict)
produto = {
    "nome": "Curso de Wordpress",
    "duração": 85,
    "preço": 10.5,
    "ativo": True,
    "tags": ["wordpress", "cms", "php"]
}

# Operadores de atribuição

# atribuição
x = 10

# atribuição com soma
x += 10

# atribuição com subtração
x -= 10

# atribuição com multiplicação
x *= 10

# atribuição com divisão
x /= 10

# atribuição com exponenciação
x **= 10

# atribuição com módulo
x %= 10

# atribuição com divisão inteira
x //= 10  

# Operadores de comparação


# imprimir texto na tela
print(nome, "é um curso de wordpress")  

#tipo de dado
print(type(nome))


# decisões com if e else 
gratuito = False

if gratuito:
    print("Curso Gratuito")
else:
    print("Curso Pago")


if not gratuito:
    print("Curso Pago")



preço = 70.00

if gratuito:
    print("Curso Gratuito")
elif preço <= 50:
    print("Curso Pago")
elif preço <= 100:
    print("Curso com preço justo")
else:
    print("Curso muito caro")


# entrada e saída de dados (input - output/print)
name = input("Digite seu nome: ")

print("Olá", name)

print(f"Olá {name}", 'seja bem vindo ao curso de wordpress')


preço_barato = input("Digite o preço do curso: ")
preço_barato = float(preço_barato)
print(preço_barato, type(preço_barato))
preço_razoavel = input("Digite o preço do curso: ")
preço_razoavel = float(preço_razoavel)

if gratuito:
    print("Curso Gratuito")
elif preço <= preço_barato:
    print("Curso Pago")
elif preço <= preço_razoavel:
    print("Curso com preço justo")
else:
    print("Curso muito caro")



# listas (list) - representar varios valores a partir de uma unca variavel
list = ["wordpress", "cms", "php"]
print(list, type(list))
print(list[0])  # mostrar o primeiro elemento da lista 
print(list[1])  # mostrar o segundo elemento da lista
print(list[2])  # mostrar o terceiro elemento da lista
print(list[-1]) # mostrar o ultimo elemento da lista

print(len(list)) # mostrar o tamanho da lista = quantidade de elementos

print(f"a lista tem {len(list)} elementos")


indice = input("Digite o indice da lista:\n ")
indice = int(indice)  # comparações precisam ser do mesmo tipo de dado

if indice < len(list):
    print(f"O curso no indice {indice} é o {list[indice]}")
else:
    print("Indice não encontrado")


# for (para) - percorrer uma lista/ repetições de tarefas
for item in list:  # item é uma variavel qualquer atribuida para mostrar o valor da lista
    print(item)

for lists in list:
    print(lists)

# criar um intervalo de numeros
for item in range(10):
    print(item)


# criar um intervalo de numeros com inicio e fim
for item in range(len(list)):
    print(list[item])

# while (enquanto) - repetições de tarefas, enquanto for verdadeira faz repetições
contador = 0
while contador < len(list):
    print(list[contador])  # faz comparações e verifica se é verdadeira
    contador = contador + 1 # incrementa o contador para não ficar em loop infinito


