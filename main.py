import mainloop


def main():
    load_success = True

    try:
        import pygame
    except ModuleNotFoundError as error:
        print(error)
        print("Pygame is required! Read README.md for installation instructions.")
        load_success = False
    try:
        import Camera
        import Polyhedron
        import Object3D
    except ModuleNotFoundError as error:
        print(error)
        print("One or more Python files are missing. Visit http://github.com/dctruesdell/Simple3DRendering "
              "to download source code.")
        load_success = False

    if not load_success:
        print("Unable to load.")
        return
    mainloop.main_loop()


if __name__ == "__main__":
    main()
