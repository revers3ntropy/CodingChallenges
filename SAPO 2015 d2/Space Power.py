"""SOLVED
Problem A. Space Power from the Computer Programming Olympiad (South Africa) SAPO 2015 day 2

'Help the Team determine the maximum power they can engage!'

11/10/21 - 14/10/21

Example:

input
3 4
5 1 3
-1 0 1
2 2 2

output
8


STEPS:
* Get user input
* Generate tree of all state changes
* Go through tree to find optimal final state
    - prune branches which don't fit with other constraints


Wasn't very difficult once I had figured out how to approach it -
as finding the best leaf node in a tree of all possibilities.
"""


class Node:
    def __init__(self, thruster, delta_thrust, parent):
        self.thruster = thruster
        self.delta_thrust = delta_thrust
        self.parent = parent

    def __repr__(self):
        out = ''
        if not self.parent:
            out += '[ROOT]'
        out += f'idx {self.thruster} +{self.delta_thrust}'
        return out

    def valid(self, S, P):
        S[self.thruster] -= 1
        P[self.thruster] += self.delta_thrust

        if not ((S[self.thruster] >= 0) and (1 >= P[self.thruster] >= -1)):
            return False

        if self.parent:
            return self.parent.valid([*S], [*P])
        else:
            return True

    def direct_children(self, nodes):
        children = []
        for child in nodes:
            if child.parent == self:
                children.append(child)

        return children

    def get_path(self):
        path: list[Node] = []

        def run(node: Node):
            path.append(node)
            if node.parent:
                run(node.parent)

        run(self)

        return path


def generate_tree(N, Q):
    nodes = []
    root_nodes = []
    leaves = []

    for i in range(N):
        for delta_thrust in range(-1, 2, 2):
            node = Node(i, delta_thrust, None)
            nodes.append(node)
            root_nodes.append(node)

    def generate_children(root, depth=0):
        if depth >= Q-1:
            leaves.append(root)
            return

        for i in range(N):
            for delta_thrust in range(-1, 2, 2):
                child = Node(i, delta_thrust, root)
                nodes.append(child)
                generate_children(child, depth + 1)

    for node in root_nodes:
        generate_children(node)

    return leaves


def value_of_path(leaf_node: Node, V, P, N) -> int:

    path = leaf_node.get_path()
    path.reverse()

    for node in path:
        P[node.thruster] += node.delta_thrust

    thrust = 0
    for i in range(N):
        thrust += V[i] * P[i]
    return thrust


def find_optimal_path(leaves, N, V, P, S):
    max_value = 0

    for leaf in leaves:
        if leaf.valid([*S], [*P]):
            value = value_of_path(leaf, [*V], [*P], N)
            if value > max_value:
                max_value = value

    return max_value


def get_n_ints(N, message=''):
    v = input(message).split(' ')
    V: list[int] = [0] * N
    for i in range(N):
        V[i] = int(v[i])
    return V


def main():
    n, q = input('N, Q: ').split(' ')
    # N: number of thrusters, Q: required state changes
    N, Q = int(n), int(q)
    # thrust per thruster
    V = get_n_ints(N, 'V: ')
    # states
    P = get_n_ints(N, 'P: ')
    # max state changes
    S = get_n_ints(N, 'S: ')

    leaves = generate_tree(N, Q)

    print(find_optimal_path(leaves, N, V, P, S))


if __name__ == '__main__':
    main()
