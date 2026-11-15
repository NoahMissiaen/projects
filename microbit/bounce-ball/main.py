paddle_x = 1
bx = 1
by = 3
dx = 1
dy = -1
launched = False
score = 0
level = 1
bricks_left = 10
bricks: List[List[number]] = []
move_timer = 0

def init_bricks():
    global bricks, bricks_left
    bricks = [[1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]]
    bricks_left = 10

def reset_ball():
    global bx, by, dx, dy, launched, move_timer
    bx = paddle_x
    by = 3
    dx = 1
    dy = -1
    launched = False
    move_timer = 0

def reset_game():
    global paddle_x, score, level
    paddle_x = 1
    score = 0
    level = 1
    init_bricks()
    reset_ball()

def draw_game():
    basic.clear_screen()
    for y in range(2):
        for x in range(5):
            if bricks[y][x] == 1:
                led.plot(x, y)
    led.plot(paddle_x, 4)
    led.plot(paddle_x + 1, 4)
    led.plot(bx, by)

def wait_for_restart():
    while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
        basic.pause(50)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(50)

reset_game()
a_ingedrukt = False
b_ingedrukt = False

while True:
    a_nu = input.button_is_pressed(Button.A)
    b_nu = input.button_is_pressed(Button.B)
    ab_nu = input.button_is_pressed(Button.AB)

    if not launched and ab_nu:
        launched = True
        dy = -1
        if paddle_x >= 2:
            dx = -1
        else:
            dx = 1
        move_timer = 10
    elif a_nu and not a_ingedrukt:
        if paddle_x > 0:
            paddle_x -= 1
    elif b_nu and not b_ingedrukt:
        if paddle_x < 3:
            paddle_x += 1

    a_ingedrukt = a_nu
    b_ingedrukt = b_nu

    if not launched:
        bx = paddle_x
        by = 3
    else:
        # Bal wordt sneller per vrijgespeeld level
        speed = 7 - level
        if speed < 3:
            speed = 3

        move_timer += 1
        if move_timer >= speed:
            move_timer = 0
            nx = bx + dx
            ny = by + dy

            # Zijwanden
            if nx < 0:
                dx = 1
                nx = bx + dx
            elif nx >= 5:
                dx = -1
                nx = bx + dx

            # Plafond
            if ny < 0:
                dy = 1
                ny = by + dy

            # Steen geraakt?
            if ny <= 1 and bricks[ny][nx] == 1:
                bricks[ny][nx] = 0
                score += 1
                bricks_left -= 1
                dy = -dy
                bx = nx

                if bricks_left == 0:
                    basic.show_string("CLEAR!")
                    level += 1
                    init_bricks()
                    reset_ball()
            elif ny == 4:
                # Paddle geraakt?
                if nx == paddle_x:
                    dy = -1
                    if bx == 0:
                        dx = 1
                    else:
                        dx = -1
                    by = 3
                elif nx == paddle_x + 1:
                    dy = -1
                    if bx == 4:
                        dx = -1
                    else:
                        dx = 1
                    by = 3
                else:
                    # Bal gemist
                    bx = nx
                    by = 4
                    draw_game()
                    basic.pause(300)
                    basic.show_string("GAME OVER")
                    basic.show_number(score)
                    wait_for_restart()
                    reset_game()
                    continue
            else:
                bx = nx
                by = ny

    draw_game()
    basic.pause(60)
