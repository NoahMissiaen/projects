lanes: List[number] = [0, 2, 4]
bg_melody: List[number] = [262, 330, 392, 330, 294, 349, 440, 392]
notes: List[List[number]] = []
score = 0
lives = 3
fall_timer = 0
spawn_steps = 0
pending_btn = 0
sound_timer = 0
melody_step = 0

def play_sfx(freq: number, ticks: number):
    global sound_timer
    music.ring_tone(freq)
    sound_timer = ticks

def reset_game():
    global notes, score, lives, fall_timer, spawn_steps, pending_btn, sound_timer, melody_step
    music.stop_all_sounds()
    notes = [[lanes[randint(0, 2)], 0]]
    score = 0
    lives = 3
    fall_timer = 0
    spawn_steps = 0
    pending_btn = 0
    sound_timer = 0
    melody_step = 0

def draw_game():
    basic.clear_screen()
    # Markerings-LEDs voor de onderste doelrij
    led.plot(1, 4)
    led.plot(3, 4)
    for n in notes:
        led.plot(n[0], n[1])

def handle_hit(target_lane: number):
    global score, lives
    hit_index = -1
    best_y = -1
    for i in range(len(notes)):
        if notes[i][0] == target_lane and notes[i][1] >= 3:
            if notes[i][1] > best_y:
                best_y = notes[i][1]
                hit_index = i
    if hit_index >= 0:
        notes.pop(hit_index)
        score += 1
        if target_lane == 0:
            play_sfx(523, 2)
        elif target_lane == 2:
            play_sfx(659, 2)
        else:
            play_sfx(784, 2)
    else:
        lives -= 1
        play_sfx(131, 3)

def play_game_over_tune():
    music.stop_all_sounds()
    music.play_tone(392, 180)
    music.play_tone(349, 180)
    music.play_tone(330, 180)
    music.play_tone(262, 350)

def wait_for_restart():
    while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
        basic.pause(50)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(50)

reset_game()
a_prev = False
b_prev = False

while True:
    # Geluid zonder vertraging weer stoppen
    if sound_timer > 0:
        sound_timer -= 1
        if sound_timer == 0:
            music.stop_all_sounds()

    a_nu = input.button_is_pressed(Button.A)
    b_nu = input.button_is_pressed(Button.B)

    # Knopdetectie met 1 tick speling voor A + B
    if pending_btn == 0:
        if (a_nu and not a_prev) and (b_nu and not b_prev):
            handle_hit(2)
        elif a_nu and not a_prev:
            pending_btn = 1
        elif b_nu and not b_prev:
            pending_btn = 2
    elif pending_btn == 1:
        pending_btn = 0
        if b_nu:
            handle_hit(2)
        else:
            handle_hit(0)
    elif pending_btn == 2:
        pending_btn = 0
        if a_nu:
            handle_hit(2)
        else:
            handle_hit(4)

    a_prev = a_nu
    b_prev = b_nu

    # Noten vallen sneller bij hogere score
    speed = 8 - Math.idiv(score, 8)
    if speed < 4:
        speed = 4

    fall_timer += 1
    if fall_timer >= speed:
        fall_timer = 0

        # Achtergrondnoot op de maat (als er geen raak/mis-geluid bezig is)
        if sound_timer == 0:
            play_sfx(bg_melody[melody_step], 1)
        melody_step = (melody_step + 1) % len(bg_melody)

        i = len(notes) - 1
        while i >= 0:
            notes[i][1] += 1
            if notes[i][1] > 4:
                notes.pop(i)
                lives -= 1
                play_sfx(131, 3)
            i -= 1

        spawn_steps += 1
        if spawn_steps >= 2:
            spawn_steps = 0
            notes.append([lanes[randint(0, 2)], 0])

    if lives <= 0:
        play_game_over_tune()
        basic.show_icon(IconNames.NO)
        basic.pause(300)
        basic.show_string("GAME OVER")
        basic.show_number(score)
        wait_for_restart()
        reset_game()
        a_prev = False
        b_prev = False
        continue

    draw_game()
    basic.pause(50)
