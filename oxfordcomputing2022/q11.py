dimensions = input().split()
width, height = int(dimensions[0]), int(dimensions[1])

black = 'X'

board = []

for i in range(height):
    board.append(list(input()))

question = 0

for y in range(height):
    for x in range(width):
        if board[y][x] == black:
            continue

        if width-1 > x > 0 and board[y][x-1] == black and board[y][x+1] != black:
            question += 1

        elif height-1 > y > 0 and board[y-1][x] == black and board[y+1][x] != black:
            question += 1

        elif y == 0 and board[y+1][x] != black:
            question += 1

        elif x == 0 and board[y][x+1] != black:
            question += 1

print(question)
