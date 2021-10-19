"""SOLVED
Problem 1 Dogs and Cats from Google Kick Start Round G 2021

'You need to determine if in this scenario all the dogs in the line will be fed'

19/10/21

Example:

input
3
6 10 4 0
CCDCDD
4 1 2 0
CCCC
4 2 1 0
DCCD


output
Case #1: YES
Case #2: YES
Case #3: NO
"""

# D: int portions of dog food
# C: int portions of cat food
# N: int animals total
# S: string is order of cats and dogs,
# where C=cat and D=dog
# fed in order
# every time a dog eats, +M cat portions
# stack of animals waiting to be fed, can only pop of top


def finishes(D: int, C: int, M: int, S: str):
    cat_food = C
    dog_food = D

    for i, animal in enumerate(S):
        if animal == 'C':
            if cat_food < 1:
                # see if there are any dogs left
                for j in range(i, len(S)):
                    if S[j] == 'D':
                        return False
            cat_food -= 1
        elif animal == 'D':
            if dog_food < 1:
                return False
            dog_food -= 1
            cat_food += M
        else:
            print('Invalid char')
    return True


def main():
    T: int = int(input())

    for testcase in range(T):
        n, d, c, m = input().split(' ')
        N, D, C, M = int(n), int(d), int(c), int(m)

        S = input()

        finished = finishes(D, C, M, S)
        res = 'NO'
        if finished:
            res = 'YES'
        print(f'Case #{testcase+1}: {res}')


if __name__ == '__main__':
    main()
