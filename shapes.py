"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.color = color
        pass

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color
        pass

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color
        pass

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius
        pass

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.radius}, color: {self.color})"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * self.radius ** 2
        pass


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side
        pass

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side
        pass


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""
    
    def __init__(self, color: str, length: float, width: float):
        super().__init__(color)
        self.width = width
        self.length = length
        pass
    
    def __repr__(self):
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"
        pass
    
    def get_area(self):
        return self.length * self.width

class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []
        pass

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)
        pass

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes
        pass

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for shape in self.shapes:
            total_area += shape.get_area()
        return total_area
        pass

    def get_circles(self) -> list:
        """Return only circles."""
        circles = [shape for shape in self.shapes if isinstance(shape, Circle)]
        return circles
        pass

    def get_squares(self) -> list:
        """Return only squares."""
        squares = [shape for shape in self.shapes if isinstance(shape, Square)]
        return squares
        pass

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles = [shape for shape in self.shapes if isinstance(shape, Rectangle)]
        return rectangles
        pass


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())
