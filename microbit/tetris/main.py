def can_place(shape: List[List[number]], bx: number, by: number):
    for block2 in shape:
        x3 = bx + block2[0]
        y3 = by + block2[1]
        if x3 < 0 or x3 >= 5:
            return False
        if y3 < 0 or y3 >= 5:
            return False
        if grid[y3][x3] == 1:
            return False
    return True

def draw(shape2: List[List[number]], bx2: number, by2: number):
    basic.clear_screen()
    for y2 in range(5):
        for x2 in range(5):
            if grid[y2][x2] == 1:
                led.plot(x2, y2)
    for block in shape2:
        x2 = bx2 + block[0]
        y2 = by2 + block[1]
        if x2 >= 0 and x2 < 5:
            if y2 >= 0 and y2 < 5:
                led.plot(x2, y2)

def new_block():
    global shape22
    shape22 = shapes[randint(0, 4)]
    return shape22

def clear_full_rows():
    global score
    y = 4
    while y >= 0:
        row_full = True
        for x in range(5):
            if grid[y][x] == 0:
                row_full = False
                break
        if row_full:
            grid.pop(y)
            grid.insert(0, [0, 0, 0, 0, 0])
            score += 1
        else:
            y -= 1

def reset_game():
    global grid, score
    grid = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]
    score = 0

score = 0
shape22: List[List[number]] = []
shapes: List[List[List[number]]] = []
grid: List[List[number]] = []
WIDTH = 5
HEIGHT = 5
shapes = [[[0, 0]],
    [[0, 0], [1, 0]],
    [[0, 0], [1, 0], [2, 0]],
    [[0, 0], [0, 1]],
    [[0, 0], [1, 0], [0, 1], [1, 1]]]

reset_game()

while True:
    shape3 = new_block()
    bx3 = 2
    by3 = 0
    if not can_place(shape3, bx3, by3):
        basic.show_string("GAME OVER")
        basic.show_number(score)
        while not input.button_is_pressed(Button.A) and not input.button_is_pressed(Button.B):
            basic.pause(50)
        reset_game()
        continue

    fall_timer = 0
    a_ingedrukt = False
    b_ingedrukt = False
    while True:
        draw(shape3, bx3, by3)
        a_nu = input.button_is_pressed(Button.A)
        b_nu = input.button_is_pressed(Button.B)

        if input.button_is_pressed(Button.AB):
            while can_place(shape3, bx3, by3 + 1):
                by3 = by3 + 1
            break
        elif a_nu and not a_ingedrukt:
            if can_place(shape3, bx3 - 1, by3):
                bx3 = bx3 - 1
        elif b_nu and not b_ingedrukt:
            if can_place(shape3, bx3 + 1, by3):
                bx3 = bx3 + 1

        a_ingedrukt = a_nu
        b_ingedrukt = b_nu

        fall_timer += 1
        if fall_timer >= 7:
            fall_timer = 0
            if can_place(shape3, bx3, by3 + 1):
                by3 = by3 + 1
            else:
                break
        basic.pause(100)

    for block3 in shape3:
        x = bx3 + block3[0]
        y = by3 + block3[1]
        grid[y][x] = 1
    clear_full_rows()
    basic.pause(200)
