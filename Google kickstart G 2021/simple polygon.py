"""
Problem 4 Simple Polygons from Google Kick Start Round G 2021

'You need to construct a simple polygon'

19/10/21

Example:

input
2
4 36
5 2



output
Case #1: POSSIBLE
2 5
6 5
8 2
0 2
Case #2: IMPOSSIBLE

Looked at the answers... had no idea where to start, turns out you needed some obscure theorem to solve.
"""
def solve(N, A) -> bool:
    return False

def main():
    T = int(input())

    for testcase in range(T):
        n, a = input().split(' ')
        N, A = int(n), int(a)

        res = solve(N, A)

        out = 'IMPOSSIBLE'
        if res:
            out = 'POSSIBLE'

        print(f'Case #{testcase+1}: {out}')


if __name__ == '__main__':
    main()
