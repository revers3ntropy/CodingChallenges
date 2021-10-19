"""SOLVED
Block Chain problem from 2019 British Informatics Olympiad Round One Question 3a

'write a program which enumerates block-chains'

4/10/21 and 5/10/21

Example:

input
4
cb

output
2


Took me ages, couldn't get the permutations thing write.
Tried to write my own code to go through all possibilities and couldn't, then tried to use the wrong itertools function

"""

from itertools import permutations

first_n_letters = int(input('I:  '))
p = input('p:  ')

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def valid_block_chain(letters):
    for i in range(len(letters)):
        for j in range(i+1, len(letters)):
            for k in range(j+1, len(letters)):

                idx1 = alphabet.index(letters[i])
                idx2 = alphabet.index(letters[j])
                idx3 = alphabet.index(letters[k])

                if idx1 < idx2 < idx3:
                    return False

    return len(set(letters)) == len(letters)


def join_tuple_string(tup):
    s = ''
    for i in tup:
        s += i
    return s


def main():
    combs = 0

    perms = list(permutations(alphabet[:first_n_letters]))

    for i in range(len(perms)):
        perms[i] = perms[i][:first_n_letters-len(p)]

    for end in set(perms):
        if valid_block_chain(p + join_tuple_string(end)):
            combs += 1

    print(combs)


if __name__ == '__main__':
    main()
