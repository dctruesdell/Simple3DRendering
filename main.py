import pygame as pg
import pygame.math as pgm
from pygame.math import Vector3, Vector2
from Polyhedron import Octahedron, Cube, Axis
from Camera import Camera


RESOLUTION = 1000, 600
BG_COLOR = "black"
FRAME_RATE = 30


OCTAHEDRON = Octahedron(Vector3(256, 256, 0), 100, (0, 0, 255))
CUBE = Cube(Vector3(256, 256, 0), 100, (255, 0, 0))
SHAPES = [OCTAHEDRON, CUBE]

ROTATE_AMOUNT = 1


def main():
    pg.init()
    screen = pg.display.set_mode(RESOLUTION)
    clock = pg.time.Clock()
    camera = Camera(pgm.Vector3(0, 0, 0), 180, screen)
    active_shape = 0

    running = True
    SHAPES[active_shape].translate(pgm.Vector3(0, 0, 50))

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    active_shape += 1
                    if active_shape > len(SHAPES):
                        active_shape = 0

        # reads full keyboard
        keys_down = pg.key.get_pressed()
        if keys_down[pg.K_UP]:
            SHAPES[active_shape].rotate(Axis.X, ROTATE_AMOUNT, True)
        elif keys_down[pg.K_DOWN]:
            SHAPES[active_shape].rotate(Axis.X, -ROTATE_AMOUNT, True)

        if keys_down[pg.K_RIGHT]:
            SHAPES[active_shape].rotate(Axis.Y, ROTATE_AMOUNT, True)
        elif keys_down[pg.K_LEFT]:
            SHAPES[active_shape].rotate(Axis.Y, -ROTATE_AMOUNT, True)

        if keys_down[pg.K_x]:
            SHAPES[active_shape].rotate(Axis.Z, ROTATE_AMOUNT, True)
        elif keys_down[pg.K_z]:
            SHAPES[active_shape].rotate(Axis.Z, -ROTATE_AMOUNT, True)


        # draw step
        screen.fill(BG_COLOR)

        camera.draw_polyhedron_wireframe(SHAPES[active_shape], 1)
        pg.display.flip()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    main()
