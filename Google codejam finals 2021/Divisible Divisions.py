"""PARTIALLY SOLVED - SLOW
Problem 4 Divisible Divisions from Google CodeJam Finals 2021

'count how many divisions of S exist that are divisible by D'

19/10/21

Example:

input
3
0145217 7
100100 10
5555 12

output
Case #1: 16
Case #2: 30
Case #3: 1

Can only do the example, all test cases take too long.
I am pretty proud of my solution, even if it is too slow.
I find divisions by looping through binary numbers 0 - 2^(length of string)
and then divide the string where the 1's are in the binary string.
"""


def valid(i: int, S: str, D: int) -> bool:
    indices = [idx for idx, val in enumerate(list(bin(i)[2:].zfill(len(S)))) if val == '1']
    if len(indices) <= 0:
        return False

    p = [S[i:j] for i, j in zip(indices, indices[1:] + [None])]

    if len(p) == 0 or len(''.join(p)) != len(S):
        return False

    for first, second in zip(p, p[1:]):
        if int(first) % D != 0 and int(second) % D != 0:
            return False
    return True


def solve(S, D) -> int:
    total = 0

    i = 0
    max = 2**len(S)
    while i < max:
        # loops over all binary numbers: 001, 010, 011 ...
        if valid(i, S, D):
            total += 1

            if total > (10**9 + 7):
                total = 0

        i += 1

    return total


def main():
    T = int(input())

    for testcase in range(T):
        S, d = input().split(' ')
        D = int(d)

        res = solve(S, D)

        print(f'Case #{testcase+1}: {res}')


if __name__ == '__main__':
    main()
