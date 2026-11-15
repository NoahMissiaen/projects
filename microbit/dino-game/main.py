dino_x = 0
dino_y = 4
jump_step = 0
jump_high = False
score = 0
obstacles: List[number] = []
move_timer = 0
spawn_timer = 0
next_spawn = 15

def reset_game():
    global dino_y, jump_step, jump_high, score, obstacles, move_timer, spawn_timer, next_spawn
    dino_y = 4
    jump_step = 0
    jump_high = False
    score = 0
    obstacles = []
    move_timer = 0
    spawn_timer = 0
    next_spawn = randint(12, 40)

def draw_game():
    basic.clear_screen()
    led.plot(dino_x, dino_y)
    for ox in obstacles:
        led.plot(ox, 4)

def is_collision():
    if dino_y == 4:
        for ox in obstacles:
            if ox == dino_x:
                return True
    return False

reset_game()

while True:
    # Springen starten (alleen als dino op de grond staat)
    if jump_step == 0:
        if input.button_is_pressed(Button.AB):
            jump_step = 1
            jump_high = True
        elif input.button_is_pressed(Button.A):
            jump_step = 1
            jump_high = False

    # Sprong uitvoeren
    if jump_step > 0:
        if not jump_high and jump_step <= 2 and input.button_is_pressed(Button.B):
            jump_high = True

        if jump_high:
            # 3 blokjes hoog (y = 1)
            if jump_step <= 2:
                dino_y = 3
            elif jump_step <= 4:
                dino_y = 2
            elif jump_step <= 12:
                dino_y = 1
            elif jump_step <= 14:
                dino_y = 2
            elif jump_step <= 16:
                dino_y = 3
            else:
                dino_y = 4
                jump_step = 0
                jump_high = False
        else:
            # 2 blokjes hoog (y = 2)
            if jump_step <= 2:
                dino_y = 3
            elif jump_step <= 11:
                dino_y = 2
            elif jump_step <= 13:
                dino_y = 3
            else:
                dino_y = 4
                jump_step = 0

        if jump_step > 0:
            jump_step += 1

    # Cactussen opschuiven (wordt langzaam sneller bij hogere score)
    speed = 6 - Math.idiv(score, 10)
    if speed < 3:
        speed = 3

    move_timer += 1
    if move_timer >= speed:
        move_timer = 0
        i = len(obstacles) - 1
        while i >= 0:
            obstacles[i] -= 1
            if obstacles[i] < 0:
                obstacles.pop(i)
                score += 1
            i -= 1

    # Nieuwe cactus op een willekeurig moment spawnen
    spawn_timer += 1
    if spawn_timer >= next_spawn:
        can_spawn = True
        for ox in obstacles:
            if ox >= 3:
                can_spawn = False
        if can_spawn:
            spawn_timer = 0
            next_spawn = randint(12, 40)
            obstacles.append(4)

    # Botsing controleren
    if is_collision():
        basic.show_string("GAME OVER")
        basic.show_number(score)
        while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
            basic.pause(50)
        while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            basic.pause(50)
        reset_game()
        continue

    draw_game()
    basic.pause(60)
