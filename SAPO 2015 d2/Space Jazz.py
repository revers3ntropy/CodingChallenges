"""SOLVED
Problem B. Space Jazz from the Computer Programming Olympiad (South Africa) SAPO 2015 day 2

'help them figure out the minimum number of notes that were left out'

15/11/21

Example:

input
aagog

output
1


STEPS:
* Generate tree of adding Q possible characters into the string at all indexes
* Check the leaf nodes for valid strings
* Repeat, incrementing Q, until a valid path is found, answer is Q

This is not a very good solution as it takes too long for even small N values.
Tried using numba, but I couldn't get it to work.
"""
import math
import time

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def round_to_sig_figs(n, sig_figs):
    return round(n, sig_figs - int(math.floor(math.log10(abs(n)))))


# VALIDATION
class NotePair:
    def __init__(self, letter, children=[]):
        self.letter = letter
        self.children = children

    def __repr__(self):
        out = self.letter + '['
        for child in self.children:
            out += child.__repr__()
        return out + ']'


class SpaceJazzValidifier:
    def __init__(self, notes: str):
        self.notes = notes
        self.idx = 0

    def step(self) -> bool:
        self.idx += 1
        return self.idx < len(self.notes)

    def parse(self, breaker_char='', depth=0):
        roots = []

        while True:
            current_char = self.notes[self.idx]

            if current_char == breaker_char:
                break

            if not self.step():
                return False

            if current_char == self.notes[self.idx]:
                roots.append(NotePair(current_char))

                if not self.step():
                    break
            else:
                res = self.parse(current_char, depth+1)
                if res is False:
                    return False

                roots.append(NotePair(current_char, res))

                if self.idx >= len(self.notes):
                    return False
                if self.notes[self.idx] != current_char:
                    return False

                if not self.step():
                    break

        if len(roots) < 1:
            return False

        return roots


# OPTIONS GENERATION
class Node:
    def __init__(self, char: str, idx: int, parent=None):
        self.char = char
        self.idx = idx
        self.parent = parent

    def __repr__(self):
        return f'+{self.char}@{self.idx}'

    def direct_children(self, nodes):
        children = []
        for child in nodes:
            if child.parent == self:
                children.append(child)

        return children

    def valid(self, letters: str) -> tuple[bool, str]:
        letters = letters[:self.idx] + self.char + letters[self.idx:]

        if self.parent:
            return self.parent.valid(letters)

        if SpaceJazzValidifier(letters).parse() is False:
            return False, letters
        return True, letters

    def apply(self, letters: str) -> str:
        letters = letters[:self.idx] + self.char + letters[self.idx:]
        if self.parent:
            letters = self.parent.apply(letters)
        return letters


def generate_tree(N: int, Q: int) -> list[Node]:
    nodes = []
    root_nodes = []
    leaves = []

    for i in range(N):
        for char in ALPHABET:
            node = Node(char, i)
            nodes.append(node)
            root_nodes.append(node)

    def generate_children(root, depth=0):
        if depth >= Q - 1:
            leaves.append(root)
            return

        for i in range(N):
            for char in ALPHABET:
                child = Node(char, i, root)
                nodes.append(child)
                generate_children(child, depth + 1)

    for node in root_nodes:
        generate_children(node)

    return leaves


def solve(letters: str):
    if SpaceJazzValidifier(letters).parse() is not False:
        return 0, letters

    Q = 0
    while True:
        Q += 1

        leaves = generate_tree(len(letters), Q)

        for leaf in leaves:
            valid, final_letters = leaf.valid(letters)
            if valid:
                return Q, final_letters


def main():
    letters = input('Notes: ')
    start = time.time()
    added, final_letters = solve(letters)
    print(f'{added} notes left out: {final_letters}')
    print(str(round_to_sig_figs(time.time() - start, 2)) + ' seconds')


if __name__ == '__main__':
    main()
