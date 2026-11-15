seq: List[number] = []
score = 0

def show_symbol(sym: number, ms: number):
    basic.clear_screen()
    if sym == 0:
        # Pijl naar links (Knop A)
        led.plot(1, 0)
        led.plot(0, 1)
        led.plot(1, 1)
        led.plot(0, 2)
        led.plot(1, 2)
        led.plot(2, 2)
        led.plot(0, 3)
        led.plot(1, 3)
        led.plot(1, 4)
    elif sym == 1:
        # Pijl naar rechts (Knop B)
        led.plot(3, 0)
        led.plot(3, 1)
        led.plot(4, 1)
        led.plot(2, 2)
        led.plot(3, 2)
        led.plot(4, 2)
        led.plot(3, 3)
        led.plot(4, 3)
        led.plot(3, 4)
    else:
        # Diamant (Knop A + B)
        led.plot(2, 0)
        led.plot(1, 1)
        led.plot(2, 1)
        led.plot(3, 1)
        led.plot(0, 2)
        led.plot(1, 2)
        led.plot(2, 2)
        led.plot(3, 2)
        led.plot(4, 2)
        led.plot(1, 3)
        led.plot(2, 3)
        led.plot(3, 3)
        led.plot(2, 4)
    basic.pause(ms)
    basic.clear_screen()

def read_button():
    while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
        basic.pause(20)
    # Korte wachttijd zodat A + B altijd samen herkend wordt
    basic.pause(70)
    a = input.button_is_pressed(Button.A)
    b = input.button_is_pressed(Button.B)
    choice = 0
    if a and b:
        choice = 2
    elif b:
        choice = 1
    else:
        choice = 0
    show_symbol(choice, 200)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(20)
    return choice

def reset_game():
    global seq, score
    seq = [randint(0, 2)]
    score = 0

def wait_for_restart():
    while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
        basic.pause(50)
    while input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
        basic.pause(50)

reset_game()

while True:
    # Reeks tonen (wordt langzaam sneller)
    show_ms = 450 - score * 15
    if show_ms < 250:
        show_ms = 250

    for step in seq:
        show_symbol(step, show_ms)
        basic.pause(180)

    # Speler speelt de reeks na
    failed = False
    for expected in seq:
        choice = read_button()
        if choice != expected:
            failed = True
            break

    if failed:
        basic.show_icon(IconNames.NO)
        basic.pause(400)
        basic.show_string("GAME OVER")
        basic.show_number(score)
        wait_for_restart()
        reset_game()
        basic.pause(300)
    else:
        score += 1
        basic.show_icon(IconNames.YES)
        basic.pause(350)
        basic.clear_screen()
        basic.pause(300)
        seq.append(randint(0, 2))
