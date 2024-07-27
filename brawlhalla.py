import pyautogui as pt
from time import sleep
import random
from pynput.keyboard import Key, Controller

from pyautogui import locateCenterOnScreen, getActiveWindowTitle, moveRel, click

# for 1080p, map specific offstage coordinates. (Big thundergard stadium)
LEFT_OFFSTAGE_X = 420
RIGHT_OFFSTAGE_X = 1500

keyboard = Controller()


def press_and_release(key: str,  presses: int = 1, interval: float = .1,) -> None:
    "Presses key, sleeps for {duration}, releases key, sleeps again."

    if presses > 1:
        while presses:
            press_and_release(key)
            presses -= 1

    elif presses == 1:
        keyboard.press(key)
        sleep(interval)
        keyboard.release(key)
        sleep(interval)

    return None


def keyDown(key: str) -> None:
    keyboard.press(key)


def keyUp(key: str) -> None:
    keyboard.release(key)


class GameCharacter:
    def __init__(self, image, left_offstage_x, right_offstage_x):
        self.image = image
        self.on_stage = True
        self.left_offstage_x = left_offstage_x
        self.right_offstage_x = right_offstage_x
        self.is_lobby_set_up = self.lobby_setup()

    def navigate_to(self, clicks, duration=0.1) -> bool:
        """Navigates cursor to the image and clicks it. Returns True if successful, otherwise False."""
        pos = locateCenterOnScreen(self.image, confidence=0.7)
        if not pos:
            print(f'{self.image} not found..')
            return False
        else:
            print(f'Moving to {self.image}')
            moveRel(pos, duration)
            sleep(0.1)
            click(clicks, interval=0.1)
            return True

    def get_character_pos(self):
        """Gets the position of the character."""
        try:
            pos = locateCenterOnScreen(self.image, confidence=0.7)
            return pos
        except Exception as e:
            # self.locate_lobby()
            print(f'{self.image} not found..')

    def is_onstage(self):
        """Tries to return character on stage, returning player state (on_stage)."""
        pos = self.get_character_pos()
        if not pos:
            return False

        if pos.x < self.left_offstage_x:
            self.on_stage = False
            key_press = 'd'
            keyDown(key_press)
        elif pos.x > self.right_offstage_x:
            self.on_stage = False
            key_press = 'a'
            keyDown(key_press)
        else:
            self.on_stage = True
            return True

        if not self.on_stage:
            print('Character is offstage')

            press_and_release(keyboard._Key.space)

            # recovery
            press_and_release('k')

            # dash
            keyDown('w')
            keyDown(keyboard._Key.shift)
            keyUp('w')
            keyUp(keyboard._Key.shift)
            return self.is_onstage()
        else:
            keyUp(key_press)
            return self.on_stage

    def handle_character_position(self):
        """Handles character position."""
        if self.is_onstage():
            self.attack()

    # rename function, fix finding map image.

    def _locate_lobby(self):
        """Returns True if in the lobby, otherwise False."""

        try:
            start_image_pos = locateCenterOnScreen(
                'images/start.png', confidence=0.7)

        except:
            print("Failed to find the image of the map.")

        else:
            print('StartMenu located! Trying to start the game..')
            self.navigate_to('images/map.png', 15)
            sleep(0.3)
            press_and_release('j', presses=3)
            return True

    def attack(self):
        """Performs an attack action."""

        # dash - sig to the right
        keyDown('d')
        keyDown(keyboard._Key.shift)
        sleep(.1)
        press_and_release('k')
        keyUp('d')
        keyUp(keyboard._Key.shift)

        # pickup/throw weapon
        press_and_release('h')

        # wait
        sleep(0.5)

        # dash - sig to the left
        keyDown('a')
        keyDown(keyboard._Key.shift)
        sleep(.1)
        press_and_release('k')
        keyUp('a')
        keyUp(keyboard._Key.shift)

        # pickup/throw weapon
        press_and_release('h')
        sleep(0.5)

    # TODO: rework

    def add_bots(self):
        """Adds bots to the game."""
        for input in list('jjjvssssssjjjjjjjvj'):
            if getActiveWindowTitle() == 'Brawlhalla':
                press_and_release(input, 1)
            else:
                return False

        # FIXME: choosing map doesnt work.
        # self.locate_lobby()

    def lobby_setup(self):
        """Returns True if lobby is set up, otherwise False."""
        try:
            settings_image_pos = locateCenterOnScreen(
                'images/x_settings.png', confidence=0.7)
        except Exception:
            print(f'failed to find set up the lobby.')
            return False

        if not settings_image_pos:
            return False

        print('trying to set up lobby')

        duration = 0.1

        # configuring settings
        for input in list('jjjjjxsssaaasaaaaaaaasaaaaaasdssssssaaaj'):
            if getActiveWindowTitle() == 'Brawlhalla':
                press_and_release(input, 1, duration)
            else:
                return False

        self.add_bots()
        self.lobby_set_up = True
        return True
