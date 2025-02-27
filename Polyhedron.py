import math
from typing import NoReturn
import pygame.math as pgm
import pygame as pg
from enum import Enum

class Axis(Enum):
    X = "x"
    Y = "y"
    Z = "z"


class Polyhedron:
    def __init__(self, position: pgm.Vector3,
                 scale_factor: [int, float],
                 draw_color: [tuple[int | float] | pg.Color | None]):
        self.position = position
        self.scale_factor = scale_factor
        self.vertices = []
        self.draw_color = draw_color

    def translate(self, translation_vector: pgm.Vector3) -> NoReturn:
        """
        Translates a point in space
        :param translation_vector: The Vector3 to move
        :return: None
        """
        self.position += translation_vector

    def rotate(self, axis: Axis, angle: [int | float], degrees: bool = False) -> NoReturn:
        """
        Rotates the polyhedron about its center
        :param axis: Axis.X, Axis.Y, or Axis.Z: The axis about which to rotate the solid
        :param angle: The angle of rotation
        :param degrees: If true, rotates by degrees. If false, rotates by radians. Uses
                        radians by default
        :return: None
        """
        if degrees:
            angle = angle * (180 / math.pi)
        new_verts = []
        # to account for the non-traditional coordinates
        cos_angle = math.cos(angle) * -1
        sin_angle = math.sin(angle) * -1
        if axis == Axis.X:
            for vertex in self.vertices:
                y = (vertex.y * cos_angle) - (vertex.z * sin_angle)
                z = (vertex.y * sin_angle) + (vertex.z * cos_angle)
                new_verts.append(pgm.Vector3(vertex.x, y, z))

        elif axis == Axis.Y:
            for vertex in self.vertices:
                x = (vertex.x * cos_angle) + (vertex.z * sin_angle)
                z = (vertex.z * cos_angle) - (vertex.x * sin_angle)
                new_verts.append(pgm.Vector3(x, vertex.y, z))

        elif axis == Axis.Z:
            for vertex in self.vertices:
                x = (vertex.x * cos_angle) - (vertex.y * sin_angle)
                y = (vertex.x * sin_angle) + (vertex.y * cos_angle)
                new_verts.append(pgm.Vector3(x, y, vertex.z))

        self.vertices = new_verts.copy()

    def scale(self, factor) -> NoReturn:
        """
        Scales a polyhedron by a scale factor
        :param factor: the amount by which to scale the solid
        :return: None
        """
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
