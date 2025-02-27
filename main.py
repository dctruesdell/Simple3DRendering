import pygame as pg


RESOLUTION = 1000, 600
BG_COLOR = "black"


def main():
    pg.init()
    screen = pg.display.set_mode(RESOLUTION)
    clock = pg.time.Clock()
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(BG_COLOR)

        pg.display.flip()


if __name__ == "__main__":
    main()
