from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self, t: "turtle.Turtle"):
        self.__t = t
        pass

    @abstractmethod
    def draw(self):
        pass
