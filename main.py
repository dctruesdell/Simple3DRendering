import pygame as pg
import pygame.math as pgm
from Polyhedron import Octahedron, Axis
from Camera import Camera


RESOLUTION = 1000, 600
BG_COLOR = "black"
FRAME_RATE = 30

OCTAHEDRON = Octahedron(pgm.Vector3(256, 256, 0), 100, (0, 0, 255))



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

        screen.fill(BG_COLOR)
        OCTAHEDRON.rotate(Axis.X, 10)
        camera.draw_polyhedron(OCTAHEDRON)
        pg.display.flip()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    main()
