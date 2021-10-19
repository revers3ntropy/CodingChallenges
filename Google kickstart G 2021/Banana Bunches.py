"""PARTIALLY SOLVED - SLOW
Problem 3 Banana Bunches from Google Kick Start Round G 2021

'How many trees should she buy?'

19/10/21

Example:

input
4
6 8
1 2 3 1 2 3
4 10
6 7 5 2
6 8
3 1 2 1 3 1
4 6
3 1 2 0


output
Case #1: 3
Case #2: -1
Case #3: 4
Case #4: 3

Test set 2 and 3 take too long to run
"""


def bunches(trees, K):
    best_cost = len(trees)+1
    found = False

    for arr1_start in range(len(trees)):

        if trees[arr1_start] == K:
            return 1

        for arr1_end in range(arr1_start, len(trees)+1):

            arr1 = trees[arr1_start:arr1_end]

            if sum(arr1) == K:
                found = True
                cost = len(arr1)
                if cost < best_cost:
                    best_cost = cost

            for arr2_start in range(arr1_end, len(trees)):
                for arr2_end in range(arr2_start, len(trees)+1):
                    arr2 = trees[arr2_start:arr2_end]

                    if sum(arr1) + sum(arr2) == K:
                        found = True
                        cost = len(arr1) + len(arr2)
                        if cost < best_cost:
                            best_cost = cost

    if not found:
        return -1

    return best_cost


def main():
    T = int(input())

    for testcase in range(T):
        n, k = input().split(' ')
        N, K = int(n), int(k)
        B = []

        b = input().split(' ')
        for str_b in b:
            B.append(int(str_b))
        B.reverse()

        res = bunches(B, K)

        print(f'Case #{testcase+1}: {res}')


if __name__ == '__main__':
    main()
