class Tree:
    def __init__(self, root=None):
        if root is None:
            self.root = 0

    def __repr__(self):
        return f"[Root:{self.root}]"


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.value = left.value + right.value

    def __repr__(self):
        return f"[Node={self.value}]"


class Leaf:
    def __init__(self, value=None):
        self.value = value

    def __repr__(self):
        return f"(Leaf={self.value})"


data = [4, 6, 9, 7, 3, 2]

all = {}

t = Tree()

# Пакуем целые числа в листья

for idx, i in enumerate(data):
    data[idx] = Leaf(i)

# Создаём словарь - key=объект : value=значение

for i in data:
    all[i] = i.value

# Ф-ия сортировки словаря по values

def sort_dict(data: dict):
    return {i:j for i, j in (sorted(data.items(), key=lambda x:(x[1])))}


# Связываем листья в узлы

while len(all) > 1:
    all = sort_dict(all)
    cur_node = Node((list(all.items())[0][0]), (list(all.items())[1][0]))
    del all[cur_node.left]
    del all[cur_node.right]
    all[cur_node] = cur_node.value


# Объявляем высший узел = root

t.root = list(all.keys())[0]

print(t.root)

def unpack(tree, binar=None):
    if binar is None:
        binar = ''

    if type(tree) == Tree:
        print(tree)

    if tree.left is not None and type(tree.left) == Node:
        print(tree.left, binar+'0')
        unpack(tree.left, binar+'0')
    elif tree.left is not None and type(tree.left) == Leaf:
        print(tree.left, binar+'0')

    if tree.right is not None and type(tree.right) == Node:
        print(tree.right, binar+'1')
        unpack(tree.right, binar+'1')
    elif tree.right is not None and type(tree.right) == Leaf:
        print(tree.right, binar+'1')


unpack(t.root)