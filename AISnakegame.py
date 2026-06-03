import random
import os
import time

# Board size
WIDTH = 20
HEIGHT = 10

# Snake starting position
snake = [[5, 5], [4, 5], [3, 5]]

# Initial direction
direction = "RIGHT"

# Food position
food = [random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1)]

score = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board():
    for y in range(HEIGHT):
        for x in range(WIDTH):

            # Draw snake
            if [x, y] in snake:
                print("■", end=" ")

            # Draw food
            elif [x, y] == food:
                print("●", end=" ")

            # Empty space
            else:
                print(".", end=" ")

        print()

def move_snake():
    global food, score

    head_x = snake[0][0]
    head_y = snake[0][1]

    # Movement
    if direction == "UP":
        head_y -= 1

    elif direction == "DOWN":
        head_y += 1

    elif direction == "LEFT":
        head_x -= 1

    elif direction == "RIGHT":
        head_x += 1

    new_head = [head_x, head_y]

    # Wall collision
    if (
        head_x < 0 or head_x >= WIDTH or
        head_y < 0 or head_y >= HEIGHT
    ):
        return False

    # Self collision
    if new_head in snake:
        return False

    snake.insert(0, new_head)

    # Food eaten
    if new_head == food:
        score += 1
        food = [random.randint(0, WIDTH-1),
                random.randint(0, HEIGHT-1)]
    else:
        snake.pop()

    return True

# Game loop
while True:

    clear()

    print("CLASSIC SNAKE GAME")
    print("Score:", score)
    print()

    draw_board()

    print()
    print("Controls: W = UP | S = DOWN | A = LEFT | D = RIGHT")

    move = input("Move: ").upper()

    if move == "W" and direction != "DOWN":
        direction = "UP"

    elif move == "S" and direction != "UP":
        direction = "DOWN"

    elif move == "A" and direction != "RIGHT":
        direction = "LEFT"

    elif move == "D" and direction != "LEFT":
        direction = "RIGHT"

    alive = move_snake()

    if not alive:
        clear()
        print("GAME OVER 😭")
        print("Final Score:", score)
        break

    time.sleep(0.1)