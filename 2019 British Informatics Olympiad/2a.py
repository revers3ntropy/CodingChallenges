"""SOLVED
Trail problem from 2019 British Informatics Olympiad Round One Question 3a

'write a program which tracks the explorer'

4/10/21

Example:

input
8
FL
9

output
(2, -1)

"""

fades_after = int(input('Fades after:  '))
program = input('Instructions:  ')
moves = int(input('Number of moves:  '))


class Trail:
    def __init__(self, x, y):
        self.age = 0
        self.x = x
        self.y = y

    def faded(self):
        return self.age > fades_after


trails = [Trail(0, 0)]


def trail_at(x, y):
    for trail in trails:
        if trail.x == x and trail.y == y:
            return not trail.faded()
    return False


rotation = 0
position = [0, 0]


def move_forwards():
    global position


def step(instruction: str, n=0):
    global rotation
    global position

    for trail in trails:
        trail.age += 1

    if instruction == 'L':
        rotation -= 1
    elif instruction == 'R':
        rotation += 1

    if rotation > 3:
        rotation = 0
    elif rotation < 0:
        rotation = 3

    move_to = [position[0], position[1]]

    if rotation == 0:
        move_to[1] += 1
    elif rotation == 1:
        move_to[0] += 1
    elif rotation == 2:
        move_to[1] -= 1
    elif rotation == 3:
        move_to[0] -= 1

    if not trail_at(move_to[0], move_to[1]):
        position = move_to
        trails.append(Trail(position[0], position[1]))
        return True
    else:
        if n < 4:
            return step('R', n + 1)
        else:
            return False


def main():
    counter = 0
    for i in range(moves):

        if not step(program[counter]):
            print('broke')
            break

        counter += 1
        if counter > len(program) - 1:
            counter = 0

        print(position, rotation)


if __name__ == '__main__':
    main()
