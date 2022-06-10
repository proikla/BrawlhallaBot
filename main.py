from brawlhalla import *

# start
# picture of username
pic_name = input('Enter the name of the image: ')
img = f'images/{pic_name}.png'
sleep(5)

# checking for active window
if pt.getActiveWindowTitle() == 'Brawlhalla':
    print("Brawlhalla is active")

# the code will be executed while the active window is 'Brawlhalla'
while pt.getActiveWindowTitle() == 'Brawlhalla':
    # if we are not in menu
    if locate_lobby() == 0:
        while True:
            pos = get_character_pos(img)
            print(pos)
            # image not found
            if pos is None:
                move_character('space', .1, 'jumping')
                break
            # image found
            else:
                x = pos.x
                y = pos.y
                print('X = ', x)
                print('Y = ', y, '\n')
                # offstage left
                if x < 420:
                    to_stage('d', con=x < 420)
                    print(type(x))
                    break
                # offstage right
                elif x > 1500:
                    to_stage('a', con=x > 1500)
                    print(type(x))
                    break
                elif x > 420 or x < 1500:
                    attack()
                    break
    # otherwise, the locateGameStart() function will start a new game.
    else:
        print('Starting new game')
