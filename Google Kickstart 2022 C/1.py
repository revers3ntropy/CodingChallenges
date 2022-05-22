def solve(p: str):
    contains_upper = False
    contains_lower = False
    contains_digit = False
    contains_special = False

    for char in p:
        if char in '0987654321':
            contains_digit = True
        elif char in 'abcdefghijklmnopqrstuvwxyz':
            contains_lower = True
        elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            contains_upper = True
        elif char in '#@*&':
            contains_special = True

    new_p = str(p)

    if not contains_lower:
        new_p += 'a'
    if not contains_upper:
        new_p += 'A'
    if not contains_digit:
        new_p += '0'
    if not contains_special:
        new_p += '#'
    if len(new_p) < 7:
        new_p += 'a' * (7 - len(new_p))

    return new_p


def main():
    T = int(input())

    for testcase in range(T):
        _ = input()
        password = input()

        res = solve(password)

        print(f'Case #{testcase + 1}: {res}')


if __name__ == '__main__':
    main()
