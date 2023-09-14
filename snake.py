import curses
import random

def draw_snake(win, snake, symbol):
    for y, x in snake:
        win.addch(y, x, symbol)

def main(stdscr):
    curses.curs_set(0)
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
  
    win.timeout(100)

    
    y, x = 10, 30
    snake = [(y, x), (y, x-1), (y, x-2)]
    food_x = random.randint(1, 58)
    food_y = random.randint(1, 18)

    win.addch(food_y, food_x, curses.ACS_PI)
    score = 0

    direction = curses.KEY_RIGHT


    while True:
        next_key = win.getch()
        direction = direction if next_key == -1 else next_key

        y, x = snake[0]

        if direction == curses.KEY_RIGHT:
            x += 1
        elif direction == curses.KEY_LEFT:
            x -= 1
        elif direction == curses.KEY_UP:
            y -= 1
        elif direction == curses.KEY_DOWN:
            y += 1

        snake.insert(0, (y, x))

        win.clear()

        # Draw boundaries
        win.hline(0, 1, '-', 58)
        win.hline(19, 1, '-', 58)
        win.vline(1, 0, '|', 18)
        win.vline(1, 59, '|', 18)

        win.addstr(0, 0, "Score:" + str(score))

        # Check if snake hit the border or itself
        if y in [0, 19] or x in [0, 59] or snake[0] in snake[1:]:
            curses.endwin()
            quit()

        

        if snake[0] == (food_y, food_x):
            food_x = random.randint(1, 58)
            food_y = random.randint(1, 18)
            score = score + 1
            

        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')

        draw_snake(win, snake, curses.ACS_CKBOARD)
        win.addch(food_y, food_x, curses.ACS_PI)

curses.wrapper(main)
