from pygame.math import Vector3, Vector2
import pygame as pg
import Polyhedron
from typing import NoReturn
from Object3D import *


class Camera(Object3D):
    def __init__(self,
                 position: Vector3,
                 focal_len: int | float,
                 screen: pg.display):
        """
        A helper class to render in 3D to a pygame display.
        :param position: The camera's position in space
        :param focal_len: The focal length of the camera, in degrees
        :param screen: The pygame display to render to
        """
        Object3D.__init__(self, position)
        self.position = position
        self.focal_len = focal_len
        self.screen = screen
        screen_size = pg.display.get_window_size()
        self.screen_offset = Vector2(screen_size[0] // 2, screen_size[1] // 2)

    def __xyz_to_xy(self, vector: Vector3) -> Vector2:
        """
        Convert a Vector3 to a 2d screen space
        :param vector: The 3d Vector to be converted
        :return: A 2d Vector representing where the input should be rendered
                in screen space
        """
        r = self.position.distance_to(vector)
        focal_ratio = self.focal_len / r
        xpos = vector.x * focal_ratio
        ypos = vector.y * focal_ratio
        return Vector2(xpos, ypos)

    def __get_screen_coords(self, poly: Polyhedron) -> list[Vector2]:
        """
        Converts a polyhedron's vertices into a list of 2d points for the camera to render
        :param poly: The polyhedron to render
        :return: A list of screen coordinates to draw to
        """
        screen_coords = []
        for vertex in poly.vertices:
            screen_coords.append(self.__xyz_to_xy(vertex + self.position) + self.screen_offset)
        return screen_coords

    def draw_polyhedron_vertices(self, poly: Polyhedron) -> NoReturn:
        """
        Draw a 3d shape
        :param poly: Any Polyhedron Object
        :return: None
        """
        screen_coords = self.__get_screen_coords(poly)

        for px in screen_coords:
            pg.draw.circle(self.screen, poly.draw_color, px, 3)

    def draw_polyhedron_wireframe(self, poly: Polyhedron, line_weight: int | float) -> NoReturn:
        screen_coords = self.__get_screen_coords(poly)
        for segment in poly.line_segments:
            pg.draw.line(self.screen, poly.draw_color,
                         screen_coords[segment[0]], screen_coords[segment[1]],
                         line_weight)

