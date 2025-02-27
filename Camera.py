import pygame.math as pgm
import pygame as pg
import Polyhedron

class Camera:
    def __init__(self, position: pgm.Vector3, focal_len: [int, float], ):
        self.position = position
        self.focal_len = focal_len

    def __xyz_to_xy(self, vector: pgm.Vector3):
        r = self.position.distance_to(vector)
        focal_ratio = self.focal_len / r
        xpos = vector.x * focal_ratio
        ypos = vector.y * focal_ratio
        return pgm.Vector2(xpos, ypos)

    def draw_polyhedron(self, screen: pg.display, poly: Polyhedra):
        screen_coords = []
        for vertex in poly.vertices:
            screen_coords.append(self.__xyz_to_xy(vertex))

        for px in screen_coords:
            pg.draw.line(screen, poly.draw_color, px, px)
