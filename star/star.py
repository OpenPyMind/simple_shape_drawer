from shape.shape import Shape


class Star(Shape):
    def __init__(self, t: "turtle.Turtle"):
        super().__init__(t)
        self.__t = t
        self.__n_points = self.__get_n_points()
        self.__size = self.__get_size()
        self.__angle = 180 - (180 / self.__n_points)

    def draw(self):
        for i in range(self.__n_points):
            self.__t.fd(self.__size)
            self.__t.lt(self.__angle)

    def __get_n_points(self):
        n_points = input("Enter number of points. 5, 7 and 9-pointed stars currently supported:")
        try:
            n_points = int(n_points)
            if n_points not in (5, 7, 9):
                raise ValueError
        except ValueError:
            return self.__get_n_points()
        return n_points

    def __get_size(self):
        size = input("Enter a valid size (min: 100, max: 300): ")
        try:
            size = int(size)
            if not (100 <= size <= 300):
                raise ValueError
        except ValueError:
            return self.__get_size()
        return size
