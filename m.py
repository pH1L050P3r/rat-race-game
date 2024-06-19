from random import randint


def mat():
    x = randint(10, 15)
    matrix = [['.']*x for i in range(x)]

    # Boundary wall
    for i in range(x):
        matrix[0][i] = '#'
        matrix[x - 1][i] = '#'
        matrix[i][0] = '#'
        matrix[i][x-1] = '#'

    # Blockage
    for i in range(1, x-1):
        size_of = randint(1, abs(i % 5)+1)
        for _ in range(size_of):
            index = randint(1, x-1)
            matrix[i][index] = '#'

    # Food
    no = (randint(1, abs((x-3-randint(1, 6)) % 7)+1)) % 10 + (x % 20)
    for _ in range(no):
        r = randint(1, x-2)
        c = randint(1, x-2)
        matrix[r][c] = '@'

    # position of j
    matrix[randint(1, x-2)][randint(1, x-2)] = 'J'
    # position of P
    matrix[randint(1, x-2)][randint(1, x-2)] = 'P'

    # buffer data
    with open('file.txt', 'w') as f:
        for _ in matrix:
            d = "".join(map(str, _)) + '\n'
            f.write(d)
            print(d, end='')
            
    return open('file.txt')
