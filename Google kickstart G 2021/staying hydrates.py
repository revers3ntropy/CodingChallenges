import math


def cost(objects, x, y):
    dist = 0

    for object in objects:
        [x1, y1], [x2, y2] = object
        closest_point = [x1, y1]
        if x <= x1:
            closest_point[0] = x1
        elif x > x2:
            closest_point[0] = x2
        else:
            closest_point[0] = x

        if y <= y1:
            closest_point[1] = y1
        elif y > y2:
            closest_point[1] = y2
        else:
            closest_point[1] = y

        dist += math.fabs(closest_point[0] - x)
        dist += math.fabs(closest_point[1] - y)

    return dist


def optimum_coords(objects):

    min = [0, 0]
    max = [100, 100]

    min_cost = cost(objects, 0, 0)
    min_pos = [0, 0]

    for [x1, y1], [x2, y2] in objects:
        if min[0] > x1:
            min[0] = x1

        if min[1] > y1:
            min[1] = y1

        if max[0] < x2:
            max[0] = x2

        if max[1] < y2:
            max[1] = y2

    for x in range(min[0], max[0]+1):
        for y in range(min[1], max[1]+1):

            current_cost = cost(objects, x, y)
            if current_cost < min_cost:
                min_cost = current_cost
                min_pos = [x, y]
            elif current_cost == min_cost:
                if x < min_pos[0]:
                    min_cost = current_cost
                    min_pos = [x, y]

                elif x == min_pos[0]:
                    if y < min_pos[1]:
                        min_cost = current_cost
                        min_pos = [x, y]

    return min_pos


def main():
    T = int(input())

    for testcase in range(T):
        K = int(input())
        objects = []

        for object_n in range(K):
            x1, y1, x2, y2 = input().split(' ')
            X1, Y1, X2, Y2 = int(x1), int(y1), int(x2), int(y2)
            objects.append([[X1, Y1], [X2, Y2]])

        x, y = optimum_coords(objects)
        print(f'Case #{testcase+1}: {x} {y}')


if __name__ == '__main__':
    main()
