"""SOLVED
Problem B. Space Robots from the Computer Programming Olympiad (South Africa) SAPO 2015 day 1

'What is the minimum time needed to complete the race, in seconds?'

4/10/21-11/10/21

Example:

input
2 2 2 5
1 1 1
100 2 1
100 2 1
100 2 1
3 4 2
400 4 4
11 4 4
5 5 5

output
25


STEPS:

* pathfinding algorithm - taking into account wait times
* store state of robots
* player position / time
* traffic light green in direction - wait times

This uses Dijkstra's Algorithm for the path finding,
which is specific for a series of weighted nodes.
Getting the axis right took ages.
Getting it to give correct weightings for roads took longer.

"""
import math


class Node:
    def __init__(self, x, y, z, u, s, w):
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.s = s
        self.w = w
        self.cost = float('inf')
        self.parent: Node = None
        self.period = self.u + self.s + self.w

    def __repr__(self):
        s = f'Node at [{self.x}, {self.y}, {self.z}], cost: {self.cost}, timers: [{self.u}, {self.s}, {self.w}], '
        if self.parent:
            s += f'parent @ [{self.parent.x}, {self.parent.y}, {self.parent.z}]'
        else:
            s += 'no parent'
        return s + '\n'

    def time_to_u(self, time):
        if time < self.u:
            return 0

        else:
            return self.period - time

    def time_to_s(self, time):
        if time < self.u:
            return self.u - time

        elif time < (self.s + self.u):
            return 0

        else:
            return self.period - time + self.u

    def time_to_w(self, time):
        if time < self.u + self.s:
            return self.u + self.s - time

        else:
            return 0


def retrace_path(start: Node, end: Node) -> list[Node]:
    path = []
    current_node = end

    while current_node != start:
        path.append(current_node)
        current_node = current_node.parent

    return list(reversed([*path, start]))


def get_neighbours(x, y, z, grid, N, M, P) -> list[Node]:
    neighbours: list[Node] = []

    if x < N-1:
        neighbours.append(grid[z][y][x+1])
    if x > 0:
        neighbours.append(grid[z][y][x-1])
    if y < M-1:
        neighbours.append(grid[z][y+1][x])
    if y > 0:
        neighbours.append(grid[z][y-1][x])
    if z < P - 1:
        neighbours.append(grid[z+1][y][x])
    if z > 0:
        neighbours.append(grid[z-1][y][x])

    return neighbours


def dist_between_neighbours(start: Node, end: Node, time, T) -> float:
    # time that it reaches the node (so that is cost + T)
    direction = [
        math.fabs(start.x - end.x),
        math.fabs(start.y - end.y),
        math.fabs(start.z - end.z)
    ]

    time %= end.period

    delay = 0

    if direction[0]:
        delay = end.time_to_u(time)
    elif direction[1]:
        delay = end.time_to_s(time)
    elif direction[2]:
        delay = end.time_to_w(time)

    return delay + T


def solve(T: int, grid: list[list[list[Node]]], N, M, P):
    # assuming start at 0, 0, 0 and end at N, M, P

    target_node = grid[N - 1][M - 1][P - 1]
    start_node = grid[0][0][0]

    open_set: list[Node] = [start_node]
    visited: list[Node] = []

    start_node.cost = 0

    def sort_open():
        open_set.sort(key=lambda x: x.cost)

    sort_open()

    while len(open_set) > 0:
        node = open_set[0]
        open_set.pop(0)
        visited.append(node)

        for neighbour in get_neighbours(node.x, node.y, node.z, grid, N, M, P):
            if neighbour not in visited:
                cost = dist_between_neighbours(node, neighbour, node.cost + T, T)
                cost += node.cost
                if cost < neighbour.cost:
                    neighbour.cost = cost
                    neighbour.parent = node
                    open_set.append(neighbour)
                    sort_open()

    return target_node.cost

"""
sample_inputs: list[list[int]] = [
    [1, 1, 1],
    [100, 2, 1],
    [100, 2, 1],
    [100, 1, 1],
    [3, 4, 2],
    [400, 4, 4],
    [11, 4, 4],
    [5, 5, 5]
]
"""

def get_input() -> tuple[int, list[list[list[Node]]], int, int, int]:
    n, m, p, t = input('>> ').split(' ')
    N, M, P, T = int(n), int(m), int(p), int(t)  # 2, 2, 2, 5

    grid: list[list[list[Node]]] = []
    for z in range(N):
        layer = []
        for y in range(M):
            row = []
            for x in range(P):
                row.append(Node(x, y, z, 0, 0, 0))
            layer.append(row)
        grid.append(layer)

    position = [0, 0, 0]
    for i in range(N * M * P):
        u, s, w = input("> ").split(' ')  # sample_inputs[i]
        node = grid[position[2]][position[1]][position[0]]
        node.u, node.s, node.w = int(u), int(s), int(w)
        node.period = node.u + node.s + node.w

        # increment position
        position[2] += 1
        if position[2] >= P:
            position[2] = 0
            position[1] += 1

            if position[1] >= M:
                position[1] = 0
                position[0] += 1

    return T, grid, N, M, P


def main():
    print(solve(*get_input()))


if __name__ == '__main__':
    main()
