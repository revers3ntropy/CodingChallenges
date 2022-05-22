def solve(N, X, Y):
    ratio = X / (Y + X)
    sequence = range(1, N + 1)
    total_sum = sum(sequence)

    target = total_sum * ratio

    if abs(target - round(target)) > 0.01:
        return False, 0, [0]

    target = round(target)

    sol = []

    start = min(target, sequence[-1])
    for i in range(start, 0, -1):
        if target - i >= 0:
            sol.append(i)
            target -= i

    if target != 0:
        return False, 0, [0]

    sol.sort()
    return True, len(sol), sol

def main():
    T = int(input())

    A = []

    for testcase in range(T):
        i = input()
        I = i.split(' ')
        A.append([int(I[0]), int(I[1]), int(I[2])])

    for i, t in enumerate(A):
        poss, l, final = solve(*t)

        pos_str = 'POSSIBLE' if poss else 'IMPOSSIBLE'
        print(f'Case #{i + 1}: {pos_str}')

        if poss:
            print(l)
            for f in final:
                print(f, end=' ')
            print()


if __name__ == '__main__':
    main()
