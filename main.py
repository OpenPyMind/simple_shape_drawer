"""An implementation of a drawing tool using the module turtle"""
import turtle

from circle.circle import Circle
from flower.flower import Flower
from polygon.polygon import Polygon
from star.star import Star


def welcome(shapes) -> str:
    welcome_msg = "Welcome to this shape-drawing program.\n" \
                  "Supported shapes:\n"
    for s in shapes:
        welcome_msg += f"-- {s}\n"

    return welcome_msg


def main():
    shapes = {
        "circle": Circle,
        "polygon": Polygon,
        "star": Star,
        "flower": Flower
              }

    print(welcome(shapes))

    while True:
        shape = input("Which shape do you want to draw? ")
        if shape in shapes:
            screen = turtle.Screen()
            pencil = turtle.Turtle()
            pencil.color("red")
            shape_inst = shapes[shape](pencil)
            shape_inst.draw()
            terminate = input("Do you want to quit? q/else: ")
            if terminate == "q":
                return
            clear_screen = input("Clear screen? y/else: ")
            if clear_screen == "y":
                screen.clear()
        else:
            print("Shape not supported.")
            break




if __name__ == '__main__':
    main()