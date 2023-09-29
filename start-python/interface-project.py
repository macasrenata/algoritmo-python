# interface

nome = input("Digite seu nome: ")

categorias = ["programação", "design", "e-commerce", "youtube"]

for i in range(len(categorias)):
    print(f"{i}. {categorias[i]}")  # 0. programação 1. design 2. e-commerce 3. youtube

num_categoria = (input("Digite o número da categoria: "))

tempo = int(input("Digite o tempo que você gostara estudar: "))

mostrar_premium = input("O curso é gratuito? (s/n): ")


# colunas da tabela em forma de lista
cursos = ["python", "javascript", "html", "css", "photoshop", "corel draw", "marketing digital", "vendas", "seo", "wordpress", "woocommerce", "dropshipping", "adsense", "youtube"]
tempos = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
gratuidades = [True, True, True, True, False]
categorias_cursos = [
    ['programação', 'python', 'backend'],
    ['programação', 'javascript', 'frontend'],
    ['programação', 'html', 'frontend'],
    ['programação', 'css', 'frontend'],
]


# processamento de dados

if mostrar_premium == "s" or gratuidades == "S":
    mostrar_premium = True
elif mostrar_premium == "n" or gratuidades == "N":
    mostrar_premium = False

num_categoria = num_categoria.split(",") # separa os elementos da lista por virgula
n_categoria = [] # lista vazia
for elemento in num_categoria: # percorre cada elemento da lista num_categoria
   numero = int(elemento.strip()) # remove os espaços em branco
   n_categoria.append(numero)  # adiciona elementos na lista n_categoria


# saida de dados

print(n_categoria) # controle de fluxo da lista numeros inteiros
print(type(n_categoria)) # controle de fluxo da lista numeros inteiros
print(f"nome: {nome}, categorias: {n_categoria}, tempo: {tempo}, gratuidade: {mostrar_premium}")



# print(f"Olá {nome}, você escolheu o curso de {categorias[num_categoria]} com duração de {tempo} horas")

# percorrer a lista e mostrar os elementos
# categorias selecionadas
categorias_selecionadas = []
for n in n_categoria:
    categorias_selecionadas.append(categorias[n].upper())

print(categorias_selecionadas)

print(f"Olá {nome}, essas são as recomendações de curso para você:")

for cat in categorias_selecionadas:
    print(f"--- {cat} ---")
    for linha in range(len(categorias_cursos)):
        if gratuidades[linha] or mostrar_premium:
          if (cat.lower() in categorias_cursos[linha]
            and tempos[linha] <= tempo):
            print(f"{cursos[linha]} ({tempos[linha]}h)")

