import os
from art import tprint
from brawlhalla import *


def get_img():
    while True:
        tprint('BrawlHallaBot', 'stop')
        service = ['start.png', 'resume.png', 'x_settings.png', 'chat.png', 'map.png']
        pics_list = os.listdir('images')
        for i in range(len(service)):
            pics_list.remove(service[i])
        pics = " ".join(pics_list)
        print(f'List of images: {pics}')
        pic_name = input('Enter the name of the image: ').strip()
        if pic_name.__contains__('.png'):
            pic_name = pic_name.strip('.png')
        image = f'images/{pic_name}.png'
        if pics_list.__contains__(f'{pic_name}.png'):
            return image
        else:
            print('This image is not exist')
            return None


if __name__ == '__main__':
    # start
    img = get_img()
    print(f'''
You chose {img}
''')
    sleep(3)
    # lobby_setup()
    # the code will be executed while the active window is 'Brawlhalla'
    while pt.getActiveWindowTitle() == 'Brawlhalla':
        locate_lobby()
        locate_map_pic()
        pos_check(img)
    print("Brawlhalla isn't active!")
    sleep(2)
