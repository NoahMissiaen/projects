px = 2
py = 2
cx = 4
cy = 4
ex = 0
ey = 0
edx = 1
edy = 1
score = 0
player_timer = 0
enemy_timer = 0
blink_timer = 0
coin_on = True

def spawn_coin():
    global cx, cy
    while True:
        nx = randint(0, 4)
        ny = randint(0, 4)
        if not (nx == px and ny == py):
            if not (ny == ey and (nx == ex or nx == ex + 1)):
                cx = nx
                cy = ny
                break

def reset_game():
    global px, py, ex, ey, edx, edy, score, player_timer, enemy_timer, blink_timer, coin_on
    px = 2
    py = 2
    ex = 0
    ey = 0
    edx = 1
    edy = 1
    score = 0
    player_timer = 0
    enemy_timer = 0
    blink_timer = 0
    coin_on = True
    spawn_coin()

def is_collision():
    if py == ey and (px == ex or px == ex + 1):
        return True
    return False

def draw_game():
    basic.clear_screen()
    # Vijand (2 LEDs breed)
    led.plot(ex, ey)
    led.plot(ex + 1, ey)
    # Knipperend muntje
    if coin_on:
        led.plot(cx, cy)
    # Speler
    led.plot(px, py)

def wait_for_restart():
    while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
        basic.pause(50)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(50)

reset_game()

while True:
    # Muntje laten knipperen
    blink_timer += 1
    if blink_timer >= 2:
        blink_timer = 0
        coin_on = not coin_on

    # Speler besturen door te kantelen
    player_timer += 1
    if player_timer >= 3:
        player_timer = 0
        ax = input.acceleration(Dimension.X)
        ay = input.acceleration(Dimension.Y)
        if ax < -250 and px > 0:
            px -= 1
        elif ax > 250 and px < 4:
            px += 1
        if ay < -250 and py > 0:
            py -= 1
        elif ay > 250 and py < 4:
            py += 1

    # Muntje gepakt?
    if px == cx and py == cy:
        score += 1
        spawn_coin()

    # Vijand stuitert sneller bij hogere score
    enemy_speed = 9 - Math.idiv(score, 3)
    if enemy_speed < 4:
        enemy_speed = 4

    enemy_timer += 1
    if enemy_timer >= enemy_speed:
        enemy_timer = 0
        ex += edx
        ey += edy
        if ex <= 0:
            ex = 0
            edx = 1
        elif ex >= 3:
            ex = 3
            edx = -1
        if ey <= 0:
            ey = 0
            edy = 1
        elif ey >= 4:
            ey = 4
            edy = -1

    if is_collision():
        draw_game()
        basic.pause(300)
        basic.show_string("GAME OVER")
        basic.show_number(score)
        wait_for_restart()
        reset_game()
        continue

    draw_game()
    basic.pause(50)
