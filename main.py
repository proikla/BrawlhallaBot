import os
from art import tprint
from brawlhalla import *


def get_img():
    while True:
        tprint('BrawlHallaBot', 'stop')
        service = ['start.png', 'resume.png']
        pics_list = os.listdir('images')
        for i in range(len(service)):
            pics_list.remove(service[i])
        pics = " ".join(pics_list)
        print(f'List of images: {pics}')
        pic_name = input('Enter the name of the image: ').strip()
        if pic_name.__contains__('.png'):
            pic_name = pic_name.strip('.png')
        image = f'images/{pic_name}.png'
        return image


if __name__ == '__main__':
    # start

    # picture of username
    img = get_img()
    print(f'''
You chose {img}
''')
    sleep(3)

    # the code will be executed while the active window is 'Brawlhalla'
    while pt.getActiveWindowTitle() == 'Brawlhalla':
        # if we are not in menu
        if locate_lobby() == 0:
            while True:
                check_pos(img)
        # otherwise, the locateGameStart() function will start a new game.
        else:
            print('Starting new game')
    print("Brawlhalla isn't active!")
    sleep(2)
