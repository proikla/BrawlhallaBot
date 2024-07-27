import os

from art import tprint
from brawlhalla import *


# as described in the README, the program will try to
# find your character on the screen using your name
# letters, so you have to turn this on in the settings.
# also, camera must be set to fixed, so your name letters
# over the top of your character are not changing in size.


# split file extension.
def split_extension(filepath):
    return os.path.splitext(filepath)[0], os.path.splitext(filepath)[1] if not os.path.isdir(filepath) else os.path.splitext(filepath)[0]


def get_img():

    # TODO: choose images more conveniently
    # 1: image1.png
    # 2: image2.png
    # ...
    # what image to use? >> 1

    # art
    tprint('BrawlHallaBot', 'stop')

    # pictures used for automated navigation in the game
    service = ['start.png', 'resume.png',
               'x_settings.png', 'chat.png', 'map.png', 'cgr.png']

    # pics used for finding character on the screen
    character_pics = os.listdir('images')

    # leave only character related pics.
    for filename in service:
        character_pics.remove(filename)

    # print out pics avaiable for finding character.
    print(f'List of images: {" ".join(character_pics)}')

    # input name of the image to use in finding character.
    pic_name = input('Enter the name of the image: ').strip().lower()

    # first filepart - name, second - extension.
    file_parts = split_extension(pic_name)

    # if user provided an extension along with the filename - strip it.
    print(file_parts)
    if file_parts[1] == '.png':
        pic_name = file_parts[0]

    image = f'images/{pic_name}.png'

    # return image path if it's a character-finding picture.
    if f'{pic_name}.png' in character_pics:
        return image
    else:
        print('This image is not exist')
        return None


# TODO: player.in_air: bool; player.below: bool
# if in_air -> dont attack.

def main():

    img = get_img()

    if img:
        print(f'''
                You chose {img}
                Now open Brawlhalla.
                ''')

    # setting up the lobby:
    while pt.getActiveWindowTitle() != 'Brawlhalla':
        print('brawlhalla isn\'t active')
        sleep(.5)

    sleep(1)

    player = GameCharacter(img, LEFT_OFFSTAGE_X, RIGHT_OFFSTAGE_X)

    # handle game movements when lobby is set up
    while True and player.is_lobby_set_up:
        if pt.getActiveWindowTitle() == 'Brawlhalla':
            player.handle_character_position()
        else:
            print('brawlhalla isn\'t active')
            sleep(.5)


if __name__ == '__main__':
    main()
