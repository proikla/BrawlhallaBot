import pyautogui as pt
from time import sleep

def nav_to_image(image, clicks, offx=0, offy=0):
    pos = pt.locateCenterOnScreen(image, confidence=.7)
    if pos is None:
        print(f'{image} not found..')
        return 0
    else:
        pt.moveTo(pos, duration=.1)
        pt.moveRel(offx, offy, duration=.1)
        pt.click(clicks=clicks, interval=.3)
def locate_menu():
    pos = pt.locateCenterOnScreen('images/resume.png', confidence=.7)
    if pos is None:
        print("resume.png not found")
        print('Trying to open the menu')

        sleep(2)
        return None
    else:
        nav_to_image('images/resume.png', 3)
        return 1
def moveCharacter(key_press, duration, action='walking'):
    pt.keyDown(key_press)
    if action == 'walking':
        print('Walking')
    if action == 'jumping':
        print('Jumping')
    if action == 'recovery':
        print('Recovery')
    if action == 'attack':
        print('attack')
    if action == 'shift':
        print('shift')
    if action == 'up':
        print('up')
    sleep(duration)
    pt.keyUp(key_press)
def getCharacterPos(image):
    pos = pt.locateCenterOnScreen(image,confidence=.7)
    if pos is None:
        print(f'{image} not found..')
        return None
    else:
        return pos
def toStage(key_press, con):
    print('OFFSTAGE!')
    pt.keyDown(key_press)
    print(f'pressed key {key_press}')
    moveCharacter('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    moveCharacter('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    moveCharacter('space', .1, 'jumping')
    if con is False:
        pt.keyUp(key_press)
    moveCharacter('k', .1, 'recovery')
    if con is False:
        pt.keyUp(key_press)
    moveCharacter('shift', 0, 'shift')
    moveCharacter('w', 0, 'up')
    pt.keyUp(key_press)
    if con is False:
        pt.keyUp(key_press)
def checkPos(image):
    while True:
        pos = getCharacterPos(image)
        print(pos)
        # IMAGE NOT FOUND
        if pos == None:
            moveCharacter('space', .1, 'jumping')
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
                toStage('d', con=x<420)
                break
            # OFFSTAGE RIGHT
            elif x > 1500:
                print(type(x))
                toStage('a', con=x>1500)
                break
            elif x > 420 or x < 1500:
                attack()
                break
            # UNDER 530
            # if y > 530:
            #     pt.keyDown('a')
            #     moveCharacter('space', .1, 'jumping')
            #     moveCharacter('space', .1, 'jumping')
            #     moveCharacter('space', .1, 'jumping')
            #     moveCharacter('k', .1, 'recovery')
            #     pt.keyUp('a')
            break
    return 0
def locateGameStart():
    pos = pt.locateCenterOnScreen('images/start.png', confidence=.7)
    if pos is None:
        pass
    else:
        print('StartMenu located! Trying to start the game..')
        for i in range(10):
            sleep(.1)
            pt.press('j')
        sleep(15)
        return 1
    return 0
def attack():
    pt.keyDown('d')
    pt.press('shift')
    moveCharacter('k',.0,'attack')
    pt.keyUp('d')
    pt.press('h')
    sleep(.5)
    pt.keyDown('a')
    pt.press('shift')
    moveCharacter('k', .0, 'attack')
    pt.keyUp('a')
    pt.press('h')