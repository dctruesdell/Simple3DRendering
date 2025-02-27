import math

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

    def translate(self, translation_vector: pgm.Vector3) -> None:
        self.position += translation_vector

    def rotate(self, axis: Axis, angle):
        new_verts = []
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        if axis == Axis.X:
            for vertex in self.vertices:
                y = (vertex.y * cos_angle) - (vertex.z * sin_angle)
                z = (vertex.y * sin_angle) + (vertex.z * cos_angle)
                new_verts.append(pgm.Vector3(vertex.x, y, z))
        self.vertices = new_verts

        if axis == Axis.Y:
            for vertex in self.vertices:
                x = (vertex.x * cos_angle) + (vertex.z * sin_angle)
                z = (vertex.z * cos_angle) - (vertex.y * sin_angle)
                new_verts.append(pgm.Vector3(x, vertex.y, z))
        self.vertices = new_verts

        if axis == Axis.Z:
            for vertex in self.vertices:
                x = (vertex.x * cos_angle) - (vertex.y * sin_angle)
                y = (vertex.y * sin_angle) + (vertex.y * cos_angle)
                new_verts.append(pgm.Vector3(x, y, vertex.z))
        self.vertices = new_verts

    # shape[i].y = (shape[i].y * rcos(deg)) - (shape[i].z * rsin(deg))
    # shape[i].z = (shape[i].y * rsin(deg)) + (shape[i].z * rcos(deg))


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
