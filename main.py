import pygame as pg
import pygame.math as pgm
from Polyhedron import Octahedron, Axis
from Camera import Camera


RESOLUTION = 1000, 600
BG_COLOR = "black"
FRAME_RATE = 30

OCTAHEDRON = Octahedron(pgm.Vector3(256, 256, 0), 100, (0, 0, 255))
ROTATE_AMOUNT = 1


def main():
    pg.init()
    screen = pg.display.set_mode(RESOLUTION)
    clock = pg.time.Clock()
    camera = Camera(pgm.Vector3(0, 0, 0), 180, screen)

    running = True
    OCTAHEDRON.translate(pgm.Vector3(0, 0, 50))

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # reads full keyboard
        keys_down = pg.key.get_pressed()
        if keys_down[pg.K_UP]:
            OCTAHEDRON.rotate(Axis.X, ROTATE_AMOUNT, True)
        elif keys_down[pg.K_DOWN]:
            OCTAHEDRON.rotate(Axis.X, -ROTATE_AMOUNT, True)

        if keys_down[pg.K_LEFT]:
            OCTAHEDRON.rotate(Axis.Y, ROTATE_AMOUNT, True)
        elif keys_down[pg.K_RIGHT]:
            OCTAHEDRON.rotate(Axis.Y, -ROTATE_AMOUNT, True)

        if keys_down[pg.K_z]:
            OCTAHEDRON.rotate(Axis.Z, ROTATE_AMOUNT, True)
        elif keys_down[pg.K_x]:
            OCTAHEDRON.rotate(Axis.X, -ROTATE_AMOUNT, True)

        # draw step
        screen.fill(BG_COLOR)

        camera.draw_polyhedron_wireframe(OCTAHEDRON, 1)
        pg.display.flip()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    main()
