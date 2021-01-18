from math import pi
from shape.shape import Shape
from polygon.polygon import Polygon


class Circle(Shape):
    def __init__(self, t: "turtle.Turtle"):
        super().__init__(t)
        self.__t = t
        self.__radius = self.__get_radius()
        self.__circumference = 2 * pi * self.__radius
        self.__n_polygon_sides = self.__get_polygon_sides()
        self.__polygon_side_length = self.__get_polygon_side_length()
        self.__circle = Polygon(
            self.__t,
            n_sides=self.__n_polygon_sides,
            side_length=self.__polygon_side_length
        )

    def draw(self):
        self.__circle.draw()

    def __get_radius(self):
        radius = input("Enter a valid radius (min: 100, max: 200): ")
        try:
            radius = int(radius)
            if not (100 <= radius <= 200):
                raise ValueError
        except ValueError:
            return self.__get_radius()
        return radius

    def __get_polygon_sides(self):
        return int(self.__circumference / 3) + 3

    def __get_polygon_side_length(self):
        return self.__circumference / self.__n_polygon_sides
