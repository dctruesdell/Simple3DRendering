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
                 scale_factor: int | float,
                 vertices: list[pgm.Vector3, ...] | None,
                 line_segments: tuple[tuple[int, int], ...] | None,
                 draw_color: tuple[int | float, ...] | pg.Color
                 ):
        """
        A class that creates a solid for the camera to draw.
        Note: vertices and line_segments should only be listed as none for pre-built shapes.
        :param position: The Polyhedron's position in 3d space
        :param scale_factor: The amount by which to scale the shape. Default shapes
                            are defined in terms of relative coordinates and must be
                            scaled to render properly.
        :param vertices: A list of vertices that define the solid
        :param draw_color:  The color to draw the shape.
        :param line_segments: A tuple of 2 index tuples that defines which vertices should be connected by the
                            renderer. The vertices are defined by their index in the vertex list.

        """
        self.position = position
        self.scale_factor = scale_factor
        self.vertices = vertices
        self.draw_color = draw_color
        self.line_segments = line_segments

    def translate(self, translation_vector: pgm.Vector3) -> NoReturn:
        """
        Translates a point in space
        :param translation_vector: The Vector3 to move
        :return: None
        """
        self.position += translation_vector

    def rotate(self, axis: Axis, angle: int | float, degrees: bool = False) -> NoReturn:
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
                 scale_factor: int | float,
                 draw_color: tuple[int | float] | pg.Color,
                 ):

        Polyhedron.__init__(self, position, scale_factor, None, None, draw_color)
        self.vertices = [pgm.Vector3(1, 0, 0),
                         pgm.Vector3(0, 1, 0),
                         pgm.Vector3(0, 0, 1),
                         pgm.Vector3(-1, 0, 0),
                         pgm.Vector3(0, -1, 0),
                         pgm.Vector3(0, 0, -1)]
        self.line_segments = ((1, 3),
                              (1, 2),
                              (1, 5),
                              (1, 0),
                              (4, 3),
                              (4, 2),
                              (4, 5),
                              (4, 0))
        self.scale(scale_factor)

