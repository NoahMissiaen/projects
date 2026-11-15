grid: List[List[number]] = []
cur_row = 4
cur_x = 0
cur_w = 3
dir_x = 1
score = 0
level = 1
move_timer = 0

def reset_tower():
    global grid, cur_row, cur_x, cur_w, dir_x, move_timer
    grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    cur_row = 4
    cur_x = -2
    cur_w = 3
    dir_x = 1
    move_timer = 0

def reset_game():
    global score, level
    score = 0
    level = 1
    reset_tower()

def draw_game():
    basic.clear_screen()
    for y in range(5):
        for x in range(5):
            if grid[y][x] == 1:
                led.plot(x, y)
    for i in range(cur_w):
        px = cur_x + i
        if px >= 0 and px < 5:
            led.plot(px, cur_row)

def wait_for_restart():
    while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
        basic.pause(50)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(50)

reset_game()
a_prev = False
b_prev = False

while True:
    a_nu = input.button_is_pressed(Button.A)
    b_nu = input.button_is_pressed(Button.B)

    if (a_nu and not a_prev) or (b_nu and not b_prev):
        if cur_row == 4:
            placed = 0
            for i in range(cur_w):
                col = cur_x + i
                if col >= 0 and col < 5:
                    grid[cur_row][col] = 1
                    placed += 1
            score += 1
            cur_w = placed
            cur_row = 3
            cur_x = -(cur_w - 1)
            dir_x = 1
        else:
            overlap = 0
            for i in range(cur_w):
                col = cur_x + i
                if col >= 0 and col < 5:
                    if grid[cur_row + 1][col] == 1:
                        grid[cur_row][col] = 1
                        overlap += 1

            if overlap == 0:
                draw_game()
                basic.pause(300)
                basic.show_string("GAME OVER")
                basic.show_number(score)
                wait_for_restart()
                reset_game()
                a_prev = False
                b_prev = False
                continue

            score += 1
            cur_w = overlap

            if cur_row == 0:
                draw_game()
                basic.pause(350)
                basic.show_string("CLEAR!")
                level += 1
                reset_tower()
            else:
                cur_row -= 1
                if randint(0, 1) == 0:
                    cur_x = -(cur_w - 1)
                    dir_x = 1
                else:
                    cur_x = 4
                    dir_x = -1

    a_prev = a_nu
    b_prev = b_nu

    # Hoog tempo: 80 ms (lvl 1) -> 60 ms (lvl 2) -> 40 ms (lvl 3+)
    speed = 5 - level
    if speed < 2:
        speed = 2

    move_timer += 1
    if move_timer >= speed:
        move_timer = 0
        min_x = -(cur_w - 1)
        max_x = 4
        cur_x += dir_x
        if cur_x <= min_x:
            cur_x = min_x
            dir_x = 1
        elif cur_x >= max_x:
            cur_x = max_x
            dir_x = -1

    draw_game()
    basic.pause(20)
