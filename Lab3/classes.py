# Exercise 1 - String Manipulation
class Exercise1:
    def __init__(self):
        self.string = ""

    def get_string(self):
        """Prompts the user to enter a string."""
        self.string = input("Enter a string: ")

    def print_string(self):
        """Prints the string in uppercase."""
        print("Upper case string:", self.string.upper())


# Exercise 2 - Shapes and Area Calculation
class Shape:
    def __init__(self):
        pass

    def area(self):
        """Method to calculate the area, returns 0 by default."""
        return 0


class Square(Shape):
    def __init__(self, side_length):
        """Initializes a square with the given side length."""
        super().__init__()
        self.side_length = side_length

    def area(self):
        """Calculates the area of the square."""
        return self.side_length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initializes a rectangle with the given length and width."""
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width


# Main execution
if __name__ == "__main__":
    # Exercise 1: String manipulation
    exercise_1 = Exercise1()
    exercise_1.get_string()
    exercise_1.print_string()

    # Exercise 2: Shape area calculations
    # Create a shape object (default shape)
    shape1 = Shape()
    print("Default shape area (no parameters):", shape1.area())

    # Create a square object with side length 7
    square1 = Square(7)
    print("Area of square with side length 7:", square1.area())

    # Create a rectangle object with length 8 and width 5
    rectangle1 = Rectangle(8, 5)
    print("Area of rectangle with length 8 and width 5:", rectangle1.area())
