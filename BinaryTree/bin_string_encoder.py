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
    def __init__(self, symb=None, value=None):
        self.symb = symb
        self.value = value

    def __repr__(self):
        return f"({self.symb}={self.value})"


text = input("Enter a string that should be encoded: ")

sym_dic = {i:text.count(i) for i in text}

print(sym_dic)

leaves = [Leaf(i, j) for i, j in sym_dic.items()]

# Создаём словарь key=объект(лист или узел), value=значение объекта

all = {i: i.value for i in leaves}


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

t = Tree()

t.root = list(all.keys())[0]

print(t.root)

code_reg = {}

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
        code_reg[tree.left.symb] = binar+'0'

    if tree.right is not None and type(tree.right) == Node:
        print(tree.right, binar+'1')
        unpack(tree.right, binar+'1')
    elif tree.right is not None and type(tree.right) == Leaf:
        print(tree.right, binar+'1')
        code_reg[tree.right.symb] = binar + '1'


unpack(t.root)

print(code_reg)

line = ''

for i in text:
    for k, j in code_reg.items():
        if i == k:
            line += j

print(line)
