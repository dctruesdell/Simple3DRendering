import pygame.math as pgm
import pygame as pg
import typing


class Polyhedron:
    def __init__(self, position: pgm.Vector3,
                 scale_factor: [int, float],
                 draw_color: [tuple[int | float] | pg.Color | None]):
        self.position = position
        self.scale_factor = scale_factor
        self.vertices = []
        self.draw_color = draw_color

    def translate(self, translation_vector: pgm.Vector3) -> None:
        self.position += translation_vector

    def scale(self, factor) -> None:
        new_verts = []
        for vertex in self.vertices:
            new_verts.append(vertex * factor)
        self.vertices = new_verts


class Octahedron(Polyhedron):

    def __init__(self, position: pgm.Vector3,
                 scale_factor: [int | float],
                 draw_color: [tuple[int | float] | pg.Color | None]):
        Polyhedron.__init__(self, position, scale_factor, draw_color)
        self.vertices = [pgm.Vector3(1, 0, 0),
                         pgm.Vector3(0, 1, 0),
                         pgm.Vector3(0, 0, 1),
                         pgm.Vector3(-1, 0, 0),
                         pgm.Vector3(0, -1, 0),
                         pgm.Vector3(0, 0, -1)]
        self.scale(scale_factor)
