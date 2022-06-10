import pyautogui as pt
from time import sleep


# moves cursor to image
def navigate_to(image, clicks, off_x=0, off_y=0):
    pos = pt.locateCenterOnScreen(image, confidence=.7)
    if pos is None:
        print(f'{image} not found..')
        return 0
    else:
        pt.moveTo(pos, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)


# exiting the pause
def locate_menu():
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
def move_character(key_press, duration, action):
    pt.keyDown(key_press)
    if action == 'walking':
        print('Walking\n')
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
def to_stage(key_press, con):
    print('OFFSTAGE!')
    pt.keyDown(key_press)
    print(f'pressed key {key_press}')
    move_character('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    move_character('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    move_character('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    move_character('k', .1, 'recovery')
    if con is False:
        pt.keyUp(key_press)
    move_character('w', 0, 'up')
    move_character('shift', 0, 'shift')
    pt.keyUp(key_press)
    if con is False:
        pt.keyUp(key_press)


# checking position
def check_pos(image):
    while True:
        pos = get_character_pos(image)
        print(pos)
        # IMAGE NOT FOUND
        if pos is None:
            move_character('space', .1, 'jumping')
            break
        # IMAGE FOUND
        else:
            x = pos.x
            y = pos.y
            print('X =', x)
            print('Y =', y, '\n')
            # OFFSTAGE LEFT
            if x < 420:
                print(type(x))
                to_stage('d', con=x < 420)
                break
            # OFFSTAGE RIGHT
            elif x > 1500:
                print(type(x))
                to_stage('a', con=x > 1500)
                break
            elif x > 420 or x < 1500:
                attack()
                break
            break
    return 0


# checking for being in the lobby
def locate_lobby():
    pos = pt.locateCenterOnScreen('images/start.png', confidence=.7)
    if pos is None:
        return 0
    else:
        print('StartMenu located! Trying to start the game..')
        for i in range(10):
            sleep(.1)
            pt.press('j')
        sleep(15)
        return 1


# speaks for itself
def attack():
    pt.keyDown('d')
    pt.press('shift')
    move_character('k', .0, 'attack')
    pt.keyUp('d')
    pt.press('h')
    sleep(.5)
    pt.keyDown('a')
    pt.press('shift')
    move_character('k', .0, 'attack')
    pt.keyUp('a')
    pt.press('h')
