import pyautogui as pt
from time import sleep

import brawlhalla as bh
#start
sleep(1)
if pt.getActiveWindowTitle() == 'Brawlhalla':
    print("Brawlhalla is active")
img = 'images/bor_1.png'
point = bh.getCharacterPos(img)
while pt.getActiveWindowTitle() == 'Brawlhalla':
    sleep(.0)
    if bh.locateGameStart() == 0:
        point = bh.getCharacterPos(img)
        while True:
            pos = bh.getCharacterPos(img)
            print(pos)
            # IMAGE NOT FOUND
            if pos is None:
                bh.moveCharacter('space', .1, 'jumping')
                break
            # IMAGE FOUND
            else:
                x = pos.x
                y = pos.y
                print('X=', x)
                print('Y=', y, '\n')
                # OFFSTAGE LEFT
                if x < 420:
                    bh.toStage('d', con=x < 420)
                    print(type(x))
                    break
                # OFFSTAGE RIGHT
                elif x > 1500:
                    bh.toStage('a', con=x > 1500)
                    print(type(x))
                    break
                elif x > 420 or x < 1500:
                    bh.attack()
                    break
    else:
        print('Starting new game')