import random
from game.shared.color import Color
from game.shared.point import Point
from game.casting.falling_object import Falling_Object

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        self._count = 0
        self._timer = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)    

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        falling_objects = cast.get_actors("falling_object")

        banner.set_text(f"Score: {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)

        # On every other frame do a movement
        self._count += 1

        if self._count == 2:

            self._count = 0

            for object in falling_objects:  
                object.move()
                if robot.get_position().equals(object.get_position()):
                    object.set_points()            
                    points = object.get_points()
                    self._score += points
                    cast.remove_actor("falling_object", object)
                    message = "Score: " + str(self._score)
                    banner.set_text(message)
                elif object.is_ready_to_delete():
                    cast.remove_actor("falling_obect", object)

        # A timer to control when to create and spawn new falling_objects
        self._timer += 1
        if self._timer == 5:

            self._timer = 0

            for n in range(30):
                rox_n_gems = [42,79]
                text = chr(random.choice(rox_n_gems))

                x = random.randint(1, 60 - 1) 
                y = random.randint(1, 40 - 1)
                position = Point(x, 3)
                position = position.scale(15)

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
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()