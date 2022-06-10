import os

from brawlhalla import *


def pic():
    banned = ['start.png', 'resume.png']
    pics_list = os.listdir('images')
    for i in range(len(banned)):
        pics_list.remove(banned[i])
    pics = " ".join(pics_list)
    print(f'List of images: {pics}')
    pic_name = input('Enter the name of the image: ').strip()
    image = f'images/{pic_name}.png'
    return image


if __name__ == '__main__':
    # start

    # picture of username
    img = pic()
    sleep(5)

    # the code will be executed while the active window is 'Brawlhalla'
    while pt.getActiveWindowTitle() == 'Brawlhalla':
        # if we are not in menu
        if locate_lobby() == 0:
            while True:
                pos = get_character_pos(img)
                check_pos(img)
        # otherwise, the locateGameStart() function will start a new game.
        else:
            print('Starting new game')
    print("Brawlhalla isn't active!")
    sleep(2)
