player_x = 2
score = 0
bullets: List[List[number]] = []
rocks: List[List[number]] = []

def reset_game():
    global player_x, score, bullets, rocks
    player_x = 2
    score = 0
    bullets = []
    rocks = []

def draw_game():
    basic.clear_screen()
    led.plot(player_x, 4)
    for b in bullets:
        led.plot(b[0], b[1])
    for r in rocks:
        led.plot(r[0], r[1])

def check_hits():
    global score
    i = len(bullets) - 1
    while i >= 0:
        bx = bullets[i][0]
        by = bullets[i][1]
        hit = False
        j = len(rocks) - 1
        while j >= 0:
            if rocks[j][0] == bx and rocks[j][1] == by:
                rocks.pop(j)
                bullets.pop(i)
                score += 1
                hit = True
                break
            j -= 1
        if hit:
            i -= 1
            continue
        i -= 1

reset_game()
rock_timer = 0
spawn_timer = 0
a_ingedrukt = False
b_ingedrukt = False
ab_ingedrukt = False

while True:
    a_nu = input.button_is_pressed(Button.A)
    b_nu = input.button_is_pressed(Button.B)
    ab_nu = input.button_is_pressed(Button.AB)

    if ab_nu and not ab_ingedrukt:
        bullets.append([player_x, 3])
    elif a_nu and not a_ingedrukt:
        if player_x > 0:
            player_x -= 1
    elif b_nu and not b_ingedrukt:
        if player_x < 4:
            player_x += 1

    a_ingedrukt = a_nu
    b_ingedrukt = b_nu
    ab_ingedrukt = ab_nu

    # Kogels gaan snel omhoog
    i = len(bullets) - 1
    while i >= 0:
        bullets[i][1] -= 1
        if bullets[i][1] < 0:
            bullets.pop(i)
        i -= 1

    check_hits()

    # Brokstukken vallen langzaam naar beneden
    rock_timer += 1
    if rock_timer >= 14:
        rock_timer = 0
        j = len(rocks) - 1
        game_over = False
        while j >= 0:
            rocks[j][1] += 1
            if rocks[j][1] >= 4:
                game_over = True
                break
            j -= 1

        if game_over:
            basic.show_string("GAME OVER")
            basic.show_number(score)
            while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
                basic.pause(50)
            reset_game()
            rock_timer = 0
            spawn_timer = 0
            continue

        check_hits()

    # Nieuw brokstuk spawnen
    spawn_timer += 1
    if spawn_timer >= 25:
        spawn_timer = 0
        rocks.append([randint(0, 4), 0])

    draw_game()
    basic.pause(80)
