from math import pi
from shape.shape import Shape


class Arc(Shape):
    def __init__(self, t: "turtle.Turtle"):
        super().__init__(t)
        self.__t = t
        self.__radius = self.__get_radius()
        self.__angle = self.__get_angle()
        self.__angle_fraction = self.__get_angle_fraction()
        self.__arc_length = self.__get_arc_length()
        self.__n_steps = self.__get_n_steps()
        self.__step_length = self.__get_step_length()
        self.__step_angle = self.__get_step_angle()

    def draw(self):
        for i in range(self.__n_steps):
            self.__t.fd(self.__step_length)
            self.__t.lt(self.__step_angle)

    def __get_radius(self):
        radius = input("Enter an arc size (min: 50, max: 150): ")
        try:
            radius = int(radius)
            if not (50 <= radius <= 150):
                raise ValueError
        except ValueError:
            return self.__get_radius()
        return radius

    def __get_angle(self):
        angle = input("Enter a valid arc angle (min: 30, max: 60): ")
        try:
            angle = int(angle)
            if not (30 <= angle <= 60):
                raise ValueError
        except ValueError:
            return self.__get_angle()
        return angle

    def __get_angle_fraction(self):
        return self.__angle / 360

    def __get_arc_length(self):
        return 2 * pi * self.__radius * self.__angle_fraction

    def __get_n_steps(self):
        return int(self.__arc_length / 3) + 1

    def __get_step_length(self):
        return self.__arc_length / self.__n_steps

    def __get_step_angle(self):
        return self.__angle / self.__n_steps

    @property
    def angle(self):
        return self.__angle


class Petal:
    def __init__(self, t: "turtle.Turtle()"):
        self.__t = t
        self.__arc = Arc(self.__t)

    def draw(self):
        for i in range(2):
            self.__arc.draw()
            self.__t.lt(180 - self.__arc.angle)

    @property
    def arc(self):
        return self.__arc


class Flower:
    def __init__(self, t: "turtle.Turtle"):
        self.__t = t
        self.__petal = Petal(self.__t)
        self.__n_petals = self.__get_n_petals()
        self.__angle_petals = self.__get_angle_petals()
        self.__angle_turn = self.__get_angle_turn()

    def draw(self):
        petals = 0
        max_petals = 360 // self.__angle_turn
        while petals < max_petals:
            self.__petal.draw()
            self.__t.lt(self.__angle_turn)
            petals += 1

    def __get_n_petals(self):
        return (360 // self.__petal.arc.angle * 2) + 1

    def __get_angle_petals(self):
        return 360 / self.__n_petals

    def __get_angle_turn(self):
        return 360 / self.__angle_petals

















