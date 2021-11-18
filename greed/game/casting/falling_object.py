from game.casting.actor import Actor
from game.shared.point import Point
import random

# TODO: Implem(ent the Artifact class here. Don't forget to inherit from Actor!
class Falling_Object(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""
        self._points = 0

    def get_points(self):
        return self._points

    def set_points(self):
        if self._text == "*":
            self._points += 100
        else:
            self._points -= 100

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message

    def move(self):
        """Move the artifacts down by a random amount between 1 and 10"""
        x = self._position.get_x()
        y = self._position.get_y()
        if y >= 600:
            y = 0 + 1
        else:
            y += 1
        self._position = Point(x,y)