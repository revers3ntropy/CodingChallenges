"""SOLVED
Problem A. Space Opera from the Computer Programming Olympiad (South Africa) SAPO 2015 day 1

5/10/21

Example 1:

input
3
3 3
2 5
1 1

output
13

Example 2:

input
5
1 3
1 8
1 9
2 4
2 5

output
14

6 hours for the whole paper. Very hard questions.
Not sure if you are allowed to use the itertools library, as it is built in as of python 2.4 or something
Time limit of 1s, memory limit of 256MB. Python might not be best language for this,
especially as you get lots of marks for making your code efficient.

"""

from itertools import permutations


def calc_profit(N: int, P: list[int], M: list[int]) -> int:
    total = 0
    current_height = 0

    for i in range(N):
        height = M[i] - current_height

        if height > 0:
            total += height * P[i]

            if M[i] > current_height:
                current_height = M[i]

    return total


def max_profit(N: int, P: list[int], M: list[int]) -> [int, tuple[int]]:
    max: int = 0
    max_order: list[int] = []

    for comb in permutations(range(N)):

        P_: list[int] = [0] * N
        M_: list[int] = [0] * N

        idx: int = 0
        for i in comb:
            P_[idx] = P[comb[i]]
            M_[idx] = M[comb[i]]
            idx += 1

        value = calc_profit(N, P_, M_)

        if value > max:
            max = value
            max_order = list(comb)

    return [max, max_order]


def get_inputs() -> tuple[int, list[float], list[int]]:
    N: int = int(input('N:  '))

    P: list[int] = [0] * N
    M: list[int] = [0] * N

    for i in range(N):
        [m, p] = input(f'{i}: ').split(' ')
        [M[i], P[i]] = [int(m), int(p)]

    return N, P, M


def main() -> None:
    print(max_profit(*get_inputs())[0])


if __name__ == '__main__':
    main()
