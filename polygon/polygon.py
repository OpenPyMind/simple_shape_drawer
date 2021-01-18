from shape.shape import Shape


class Polygon(Shape):
    def __init__(self, t: "turtle.Turtle", **kwargs):
        super().__init__(t)
        self.__t = t
        if not kwargs:
            self.__n_sides = self.__get_n_sides()
            self.__side_length = self.__get_side_length()
        else:
            self.__n_sides = kwargs["n_sides"]
            self.__side_length = kwargs["side_length"]
        self.__angle = self.__get_angle()

    def draw(self):
        for i in range(self.__n_sides):
            self.__t.fd(self.__side_length)
            self.__t.lt(self.__angle)

    def __get_n_sides(self):
        n = input("Enter the number of sides (min: 3): ")
        try:
            n = int(n)
            if n < 3:
                raise ValueError
        except ValueError:
            return self.__get_n_sides()
        return n

    def __get_side_length(self):
        side_length = input("Enter a valid side length (min: 100, max: 300): ")
        try:
            side_length = int(side_length)
            if not (100 <= side_length <= 300):
                raise ValueError
        except ValueError:
            return self.__get_side_length()
        return side_length

    def __get_angle(self):
        return 360 / self.__n_sides

