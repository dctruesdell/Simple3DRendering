from pygame.math import Vector3, Vector2
from enum import Enum
from typing import NoReturn


class Axis(Enum):
    X = "x"
    Y = "y"
    Z = "z"


class Object3D:
    def __init__(self, position: Vector3):
        """
        A template class for any other 3D object, such as the Camera and Polyhedron classes.
        :param position: The object's position in 3D space.
        """
        self.position = position

    def translate(self, translation_vector: Vector3) -> NoReturn:
        """
        Translates a point in space
        :param translation_vector: The Vector3 to move
        :return: None
        """
        self.position += translation_vector
