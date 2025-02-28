import pygame.math as pgm
import pygame as pg
import Polyhedron
from typing import NoReturn


class Camera:
    def __init__(self,
                 position: pgm.Vector3,
                 focal_len: int | float,
                 screen: pg.display):
        self.position = position
        self.focal_len = focal_len
        self.screen = screen
        screen_size = pg.display.get_window_size()
        self.screen_offset = pgm.Vector2(screen_size[0] // 2, screen_size[1] // 2)

    def __xyz_to_xy(self, vector: pgm.Vector3) -> pgm.Vector2:
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
        return pgm.Vector2(xpos, ypos)

    def draw_polyhedron_vertices(self, poly: Polyhedron) -> NoReturn:
        """
        Draw a 3d shape
        :param poly: Any Polyhedron Object
        :return: None
        """
        screen_coords = []
        for vertex in poly.vertices:
            screen_coords.append(self.__xyz_to_xy(vertex))

        for px in screen_coords:
            pg.draw.circle(self.screen, poly.draw_color, px + self.screen_offset, 3)

