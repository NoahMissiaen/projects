snake: List[List[number]] = []
dx = 1
dy = 0
next_turn = 0
food: List[number] = [4, 2]
score = 0
move_timer = 0
blink_timer = 0
food_on = True

def on_snake(tx: number, ty: number):
    for seg in snake:
        if seg[0] == tx and seg[1] == ty:
            return True
    return False

def spawn_food():
    global food
    free: List[List[number]] = []
    for x in range(5):
        for y in range(5):
            if not on_snake(x, y):
                free.append([x, y])
    if len(free) > 0:
        food = free[randint(0, len(free) - 1)]

def reset_game():
    global snake, dx, dy, next_turn, score, move_timer, blink_timer, food_on
    snake = [[2, 2], [1, 2], [0, 2]]
    dx = 1
    dy = 0
    next_turn = 0
    score = 0
    move_timer = 0
    blink_timer = 0
    food_on = True
    spawn_food()

def draw_game():
    basic.clear_screen()
    for seg in snake:
        led.plot(seg[0], seg[1])
    if food_on:
        led.plot(food[0], food[1])

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

    if a_nu and not a_ingedrukt:
        next_turn = -1
    elif b_nu and not b_ingedrukt:
        next_turn = 1

    a_ingedrukt = a_nu
    b_ingedrukt = b_nu

    # Voedsel laten knipperen
    blink_timer += 1
    if blink_timer >= 2:
        blink_timer = 0
        food_on = not food_on

    # Snelheid gaat omhoog naarmate je score stijgt
    speed = 8 - Math.idiv(score, 4)
    if speed < 4:
        speed = 4

    move_timer += 1
    if move_timer >= speed:
        move_timer = 0

        if next_turn == -1:
            ndx = dy
            ndy = -dx
            dx = ndx
            dy = ndy
        elif next_turn == 1:
            ndx = -dy
            ndy = dx
            dx = ndx
            dy = ndy
        next_turn = 0

        nx = snake[0][0] + dx
        ny = snake[0][1] + dy

        # Botsing met rand?
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            basic.show_string("GAME OVER")
            basic.show_number(score)
            wait_for_restart()
            reset_game()
            continue

        ate_food = (nx == food[0] and ny == food[1])
        if not ate_food:
            snake.pop()

        # Botsing met eigen lichaam?
        if on_snake(nx, ny):
            basic.show_string("GAME OVER")
            basic.show_number(score)
            wait_for_restart()
            reset_game()
            continue

        snake.insert(0, [nx, ny])

        if ate_food:
            score += 1
            if len(snake) == 25:
                basic.show_string("YOU WIN!")
                basic.show_number(score)
                wait_for_restart()
                reset_game()
                continue
            spawn_food()

    draw_game()
    basic.pause(60)
