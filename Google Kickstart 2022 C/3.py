def solve(stick, L):

    while True:
        for i in range(L+1):
            if stick[i] == 0:
                continue

            if stick[i] == 1:
                if i == L:
                    stick[i] = 0



def main():
    T = int(input())

    for testcase in range(T):
        N, L = map(int, input().split(' '))

        stick = [0] * (L+1)

        for n in range(N):
            Pi, Di = map(int, input().split(' '))
            stick[Pi] = 1 if Di == 1 else -1

        res = solve(stick, L)

        print(f'Case #{testcase + 1}: {res}')


if __name__ == '__main__':
    main()