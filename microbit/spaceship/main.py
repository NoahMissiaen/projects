bird_x = 1
bird_y = 2
score = 0
pipes: List[List[number]] = []
pipe_timer = 0
spawn_steps = 0

def reset_game():
    global bird_y, score, pipes, pipe_timer, spawn_steps
    bird_y = 2
    score = 0
    pipes = [[4, randint(0, 4)]]
    pipe_timer = 0
    spawn_steps = 0

def draw_game():
    basic.clear_screen()
    for p in pipes:
        px = p[0]
        gap = p[1]
        for y in range(5):
            if y != gap:
                led.plot(px, y)
    led.plot(bird_x, bird_y)

def is_collision():
    for p in pipes:
        if p[0] == bird_x:
            if bird_y != p[1]:
                return True
    return False

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
        if bird_y > 0:
            bird_y -= 1
    elif b_nu and not b_ingedrukt:
        if bird_y < 4:
            bird_y += 1

    a_ingedrukt = a_nu
    b_ingedrukt = b_nu

    if is_collision():
        basic.show_string("GAME OVER")
        basic.show_number(score)
        wait_for_restart()
        reset_game()
        continue

    # Buizen verschuiven (wordt langzaam sneller)
    speed = 8 - Math.idiv(score, 6)
    if speed < 4:
        speed = 4

    pipe_timer += 1
    if pipe_timer >= speed:
        pipe_timer = 0
        i = len(pipes) - 1
        while i >= 0:
            pipes[i][0] -= 1
            if pipes[i][0] < 0:
                pipes.pop(i)
                score += 1
            i -= 1

        spawn_steps += 1
        if spawn_steps >= 3:
            spawn_steps = 0
            pipes.append([4, randint(0, 4)])

        if is_collision():
            basic.show_string("GAME OVER")
            basic.show_number(score)
            wait_for_restart()
            reset_game()
            continue

    draw_game()
    basic.pause(60)
