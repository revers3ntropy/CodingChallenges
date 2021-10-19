"""SOLVED
Problem C. Towers from the Computer Programming Olympiad (South Africa) SAPO 2015 day 1

'Help Spock solve the Lombax Mystery'

4/10/21-11/10/21

Example:

input
4 5
-1 0 1 0
1 -1 1 0
0 0 1
1 3 7
1 1 1
0 1 2
0 0 8

output
3
1
1

"""


class Node:
    def __init__(self, index, number, children: list):
        self.index = index
        self.number = number
        self.children = children

    def all_children(self) -> list:
        res = []
        for child in self.children:
            res.append(child)
            for subchild in child.all_children():
                res.append(subchild)
        return res

    def __repr__(self):
        return f'Node {self.index}: {self.number} with children {str([i for i in map(lambda n: n.index, self.children)])}\n'


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def get_nodes(self):
        return [self.root, *self.root.all_children()]

    def node_from_idx(self, idx: int) -> Node:
        for child in self.get_nodes():
            if child.index == idx:
                return child
        print('No child found')


def num_paths(tree: Tree, v, W) -> int:
    paths = 0

    def recurse(node, path_total):
        nonlocal paths
        if node.number + path_total == W:
            paths += 1

        for child in node.children:
            recurse(child, path_total + node.number)

    recurse(tree.node_from_idx(v), 0)

    return paths


def solve_q(tree: Tree, mode: int, v: int, W: int):
    if mode == 0:
        return num_paths(tree, v, W)

    tree.node_from_idx(v).number = W
    return None

"""
example_input = [
    [0, 0, 1],
    [1, 3, 7],
    [1, 1, 1],
    [0, 1, 2],
    [0, 0, 8]
]
"""

def main():
    n, q = input('N, Q: ').split(' ')
    N, Q = int(n), int(q) #4, 5

    nodes = [Node(i, 0, []) for i in range(N)]
    root = None

    t = input('T: ').split(' ') # [-1, 0, 1, 0]
    # T[i] is parent of i
    T: list[int] = [0] * N
    for i in range(N):
        T[i] = int(t[i])
        if T[i] != -1:
            nodes[T[i]].children.append(nodes[i])
        else:
            root = nodes[i]

    l = input('L: ').split(' ') #[1, -1, 1, 0]
    # L[i] is number above i
    L: list[int] = [0] * N
    for i in range(N):
        L[i] = int(l[i])
        nodes[i].number = L[i]

    tree = Tree(root)

    out = []

    for j in range(Q):
        mode_, v_, W_ = input().split(' ')  #example_input[j]
        mode, v, W = int(mode_), int(v_), int(W_)

        res = solve_q(tree, mode, v, W)
        if res is not None:
            out.append(res)

    for line in out:
        print(line)


if __name__ == '__main__':
    main()
