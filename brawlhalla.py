import pyautogui as pt
from time import sleep


# moves cursor to image
def navigate_to(image, clicks, off_x=0, off_y=0):
    pos = pt.locateCenterOnScreen(image, confidence=.7)
    if pos is None:
        print(f'{image} not found..')
        return 0
    else:
        print(f'Moving to {image}')
        pt.moveTo(pos, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)


def image_check(image):
    if image is None:
        print("resume.png not found")
        print('Trying to open the menu')
        sleep(2)
        return None
    else:
        navigate_to('images/resume.png', 3)
        return 1


# exiting the pause (unused)
def locate_pause_menu():
    pos = pt.locateCenterOnScreen('images/resume.png', confidence=.7)
    if pos is None:
        print("resume.png not found")
        print('Trying to open the menu')
        sleep(2)
        return None
    else:
        navigate_to('images/resume.png', 3)
        return 1


# moves character
def do_input(key_press, duration, action=''):
    pt.keyDown(key_press)
    if action == 'jumping':
        print('Jumping\n')
    if action == 'recovery':
        print('Recovery\n')
    if action == 'attack':
        print('attack\n')
    if action == 'shift':
        print('shift\n')
    if action == 'up':
        print('up\n')
    sleep(duration)
    pt.keyUp(key_press)


# getting position of the character
def get_character_pos(image):
    pos = pt.locateCenterOnScreen(image, confidence=.7)
    if pos is None:
        print(f'{image} not found..')
        return None
    else:
        return pos


# comes back to stage
def to_stage(stage, con):
    if stage == 'left':
        key_press = 'd'
    elif stage == 'right':
        key_press = 'a'
    else:
        key_press = ''
    print('Character on offstage')
    pt.keyDown(key_press)
    print(f'pressed key {key_press}')
    do_input('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    do_input('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    do_input('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    do_input('k', .1, 'recovery')
    if con is False:
        pt.keyUp(key_press)
    do_input('w', 0, 'up')
    do_input('shift', 0, 'shift')
    pt.keyUp(key_press)
    if con is False:
        pt.keyUp(key_press)


# checking character position
def pos_check(image):
    while True:
        pos = get_character_pos(image)
        print(pos)
        # IMAGE NOT FOUND
        if pos is None:
            do_input('space', .1, 'jumping')
            break
        # IMAGE FOUND
        else:
            x = pos.x
            y = pos.y
            print('X =', x)
            print('Y =', y, '\n')
            # OFFSTAGE LEFT
            if x < 420:
                to_stage('left', con=x < 420)
                break
            # OFFSTAGE RIGHT
            elif x > 1500:
                to_stage('right', con=x > 1500)
                break
            elif x > 420 or x < 1500:
                attack()
                break
            break
    return 0


# new stuff
def locate_map_pic():
    print('Trying to find map.png on screen')
    map_pic = 'images/map.png'
    navigate_to(map_pic, 5)
    pt.press('j')


# checking for being in the lobby
def locate_lobby():
    pos = pt.locateCenterOnScreen('images/start.png', confidence=.7)
    if pos is None:
        return 0
    else:
        print('StartMenu located! Trying to start the game..')
        sleep(5)
        for i in range(6):
            sleep(.1)
            pt.press('j')
        sleep(2)
        return 1


# speaks for itself
def attack():
    pt.keyDown('d')
    pt.press('shift')
    do_input('k', .0, 'attack')
    pt.keyUp('d')
    pt.press('h')
    sleep(.5)
    pt.keyDown('a')
    pt.press('shift')
    do_input('k', .0, 'attack')
    pt.keyUp('a')
    pt.press('h')


def add_bots():
    pt.press('v')
    duration = .4
    sleep(duration)
    for _ in range(7):
        pt.press('j')
        sleep(duration)
        pt.press('j')
        sleep(duration)
        pt.press('s')
        sleep(duration)
        pt.press('a')
        sleep(duration)
        pt.press('j')
        sleep(duration)
        pt.press('s')
        sleep(duration)
    sleep(duration)
    pt.press('v')


def lobby_setup():
    settings_image = pt.locateCenterOnScreen('images/x_settings.png', confidence=.7)
    if settings_image is None:
        print(f'x_settings.png not found..')
        return None
    else:
        duration = .0
        # open settings tab
        pt.press('x')
        for _ in range(2):
            pt.press('s')
            sleep(duration)
        # lives
        for _ in range(3):
            pt.press('a')
            sleep(duration)
        pt.press('s')
        # match time
        for _ in range(8):
            pt.press('a')
            sleep(duration)
        pt.press('s')
        # damage
        for _ in range(6):
            pt.press('a')
            sleep(duration)
        for _ in range(5):
            pt.press('s')
            sleep(duration)
        for _ in range(3):
            pt.press('a')
            sleep(duration)
        pt.press('j')
        pt.press('j')
        pt.press('j')
        add_bots()
