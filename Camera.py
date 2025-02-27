import pygame.math as pgm
import pygame as pg
import Polyhedron


class Camera:
    def __init__(self,
                 position: pgm.Vector3,
                 focal_len: [int, float],
                 screen: pg.display):
        self.position = position
        self.focal_len = focal_len
        self.screen = screen
        screen_size = pg.display.get_window_size()
        self.screen_offset = pgm.Vector2(screen_size[0] // 2, screen_size[1] // 2)

    def __xyz_to_xy(self, vector: pgm.Vector3):
        r = self.position.distance_to(vector)
        focal_ratio = self.focal_len / r
        xpos = vector.x * focal_ratio
        ypos = vector.y * focal_ratio
        return pgm.Vector2(xpos, ypos)

    def draw_polyhedron(self, poly: Polyhedron):
        screen_coords = []
        for vertex in poly.vertices:
            screen_coords.append(self.__xyz_to_xy(vertex))

        for px in screen_coords:
            pg.draw.circle(self.screen, poly.draw_color, px + self.screen_offset, 3)
