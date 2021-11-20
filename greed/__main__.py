import os
import random

from game.casting.actor import Actor
from game.casting.falling_object import Falling_Object
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 30
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_OBJECTS = 30


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(45)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("<^>")
    robot.set_font_size(25)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the rocks and gems

    for n in range(DEFAULT_OBJECTS):
        rox_n_gems = [42,79]
        text = chr(random.choice(rox_n_gems))

        x = random.randint(1, COLS - 1) 
        y = random.randint(1, ROWS - 1)
        position = Point(x, 3)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        falling_object = Falling_Object()
        falling_object.set_text(text)
        falling_object.set_font_size(30)
        falling_object.set_color(color)
        falling_object.set_position(position)
        cast.add_actor("falling_object", falling_object)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()