class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        if balance < -1:
            if key > root.right.key:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self._get_min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        if balance > 1:
            if self._get_balance(root.left) >= 0:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        if balance < -1:
            if self._get_balance(root.right) <= 0:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_min_value_node(self, root):
        if root is None or root.left is None:
            return root
        return self._get_min_value_node(root.left)

    def _preorder(self, root):
        if not root:
            return
        print(f"{root.key}", end=" ")
        self._preorder(root.left)
        self._preorder(root.right)

    def preorder(self):
        self._preorder(self.root)


# Exemplo de uso
tree = AVLTree()

while True:
    operation, *values = input().split()
    
    if operation == "insert":
        key = int(values[0])
        tree.insert(key)
    elif operation == "delete":
        key = int(values[0])
        tree.delete(key)
    elif operation == "search":
        key = int(values[0])
        if tree.search(key):
            print(f"Chave {key} encontrada na árvore")
        else:
            print(f"Chave {key} não encontrada na árvore")
    elif operation == "preorder":
        tree.preorder()
        print()
    elif operation == "quit":
        break
    else:
        print("Operação inválida")


    # Neste código, a função AVLTree define a classe da Árvore AVL, e a função Node define a classe dos nós da árvore. 
    # As operações de inserção, exclusão e busca são implementadas com os métodos insert, delete e search, respectivamente. 
    # A função _rotate_left é responsável por realizar rotações simples à esquerda, e a função _rotate_right realiza rotações simples à direita.
    # A função preorder é utilizada para imprimir a árvore em pré-ordem, para visualização dos resultados após cada operação.

    # Para executar o programa, você pode digitar o seguinte comando no terminal:
    # python3 or python arvore_avl.py

    # Agora você pode interagir com ele digitando os comandos no formato "operacao chave" e pressionando Enter no terminal
    # Para encerrar o programa, você pode digitar: quit