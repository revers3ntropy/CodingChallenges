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
