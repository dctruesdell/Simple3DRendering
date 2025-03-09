import pygame as pg
from settings import Controls
from pygame.math import Vector3
from Polyhedron import Octahedron, Cube
from Object3D import Axis
from Camera import Camera


RESOLUTION = 1000, 600
BG_COLOR = "black"
FRAME_RATE = 30
FOCAL_LEN = 270

OCTAHEDRON = Octahedron(Vector3(256, 256, 0), 100, (0, 0, 255))
CUBE = Cube(Vector3(256, 256, 0), 100, (255, 0, 0))
SHAPES = [OCTAHEDRON, CUBE]

ROTATE_AMOUNT = 1
MOVE_SPEED = 15


def main_loop():
    pg.init()
    screen = pg.display.set_mode(RESOLUTION)

    clock = pg.time.Clock()
    camera = Camera(Vector3(0, 0, 0), FOCAL_LEN, screen)
    active_shape = 0

    # title screen text
    font = pg.font.SysFont("Courier New", 24)
    text = font.render(f"{"-" * 20}\nSimple3DRenderer By Diana Truesdell\n2025\n{"-" * 20}",
                       False,
                       (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (RESOLUTION[0] // 2, RESOLUTION[1] // 2)

    screen.blit(text, text_rect)
    pg.display.flip()

    title_screen = True
    while title_screen:
        keys_down = pg.key.get_pressed()
        for event in pg.event.get():
            if keys_down[Controls.CONTINUE]:
                title_screen = False
            if event.type == pg.QUIT:
                return

    running = True
    SHAPES[active_shape].translate(Vector3(0, 0, 1))
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    active_shape += 1
                    if active_shape >= len(SHAPES):
                        active_shape = 0

        # reads full keyboard
        keys_down = pg.key.get_pressed()

        # -- rotations --
        if keys_down[Controls.ROT_X_POS]:
            SHAPES[active_shape].rotate(Axis.X, ROTATE_AMOUNT, True)
        elif keys_down[Controls.ROT_X_NEG]:
            SHAPES[active_shape].rotate(Axis.X, -ROTATE_AMOUNT, True)

        if keys_down[Controls.ROT_Y_POS]:
            SHAPES[active_shape].rotate(Axis.Y, ROTATE_AMOUNT, True)
        elif keys_down[Controls.ROT_Y_NEG]:
            SHAPES[active_shape].rotate(Axis.Y, -ROTATE_AMOUNT, True)

        if keys_down[Controls.ROT_Z_POS]:
            SHAPES[active_shape].rotate(Axis.Z, ROTATE_AMOUNT, True)
        elif keys_down[Controls.ROT_Z_NEG]:
            SHAPES[active_shape].rotate(Axis.Z, -ROTATE_AMOUNT, True)

        # -- camera movement --
        if keys_down[Controls.MOVE_FORWARD]:
            camera.translate(Vector3(0, 0, MOVE_SPEED))
        elif keys_down[Controls.MOVE_LEFT]:
            camera.translate(Vector3(0, 0, -MOVE_SPEED))

        if keys_down[Controls.MOVE_BACKWARD]:
            camera.translate(Vector3(MOVE_SPEED, 0, 0))
        elif keys_down[Controls.MOVE_RIGHT]:
            camera.translate(Vector3(-MOVE_SPEED, 0, 0))

        if keys_down[Controls.ROT_CAM_POS]:
            camera.rotation += 1
        elif keys_down[Controls.ROT_CAM_NEG]:
            camera.rotation -= 1

        # draw step
        screen.fill(BG_COLOR)

        camera.draw_polyhedron_wireframe(SHAPES[active_shape], 1)
        pg.display.flip()
        clock.tick(FRAME_RATE)

