"""SOLVED
Trail problem from 2019 British Informatics Olympiad Round One Question 3a

'write a program which reads in a positive integer of up to 20 digits'

4/10/21

Examples:
17 => 22
343 => 353

"""


def reverse_string(s):
    out = ''
    for i in range(len(s)):
        out += s[len(s)-i-1]
    return out


def is_palindromic(n_):
    n_str = str(n_)
    return n_str == reverse_string(n_str)


def find(above):
    n = above

    while 1:
        n += 1
        if is_palindromic(n):
            break

    return n


def main():
    n = int(input('Enter a number:  '))
    if len(str(n)) <= 20:
        print(find(n))
    else:
        print('Number must be less than 20 characters')
        main()


if __name__ == '__main__':
    main()
