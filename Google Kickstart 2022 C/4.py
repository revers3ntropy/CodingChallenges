def solve():
    pass


def main():
    T = int(input())

    for testcase in range(T):
        _ = input().split(' ')

        res = solve()

        print(f'Case #{testcase + 1}: {res}')


if __name__ == '__main__':
    main()