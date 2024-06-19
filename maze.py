import random
import controll


def random_maze():
    file = open('maze.txt', 'w', encoding='UTF-8')
    side = random.randint(10, 20)
    maze = [[controll.HALL]*side for i in range(side)]
    for i in range(side):
        maze[0][i] = controll.WALL
        maze[side - 1][i] = controll.WALL
        maze[i][0] = controll.WALL
        maze[i][side-1] = controll.WALL

# Blocks
    for i in range(1, side-1):
        for _ in range(random.randint(1, (side % 5)+1)):
            index = random.randint(1, side-1)
            maze[i][index] = controll.WALL

# Food
    food_items = (random.randint(1, abs((side-3-random.randint(1, 6))%7)+1))%10 + (side%40)
    for _ in range(food_items):
        row = random.randint(1, side-2)
        col = random.randint(1, side-2)
        maze[row][col] = controll.SPROUT

# Position Of J
    maze[random.randint(1, side-2)][random.randint(1, side-2)] = controll.RAT_1_CHAR
# Position Of P
    maze[random.randint(1, side-2)][random.randint(1, side-2)] = controll.RAT_2_CHAR

# buffer data
    for _ in maze:
        file.write("".join(map(str, _))+'\n')

    file.close()


random_maze()
