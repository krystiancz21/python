from typing import Union

class Rectangle:
    """
    A class representing a rectangle.
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    area = 0

    def __init__(self, width: Union[int, float], height: Union[int, float]) -> None:
        """
        Initialize a new Rectangle instance.

        Args:
            width ([int, float]): The width of the rectangle.
            height ([int, float]): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self) -> Union[int, float]:
        """
        Get the width of the rectangle.

        Returns:
            [int, float]: The current width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, width: Union[int, float]) -> None:
        """
        Set the width of the rectangle.

        Args:
            width (Union[int, float]): The new width value.
        """
        if width > 0:
            self.__width = width
        else:
            raise ValueError("Width must be greater than 0!")

    @property
    def height(self) -> Union[int, float]:
        """
        Get the height of the rectangle.

        Returns:
            Union[int, float]: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height: Union[int, float]) -> None:
        """
        Set the height of the rectangle.

        Args:
            height (Union[int, float]): The new height value.
        """
        if height > 0:
            self.__height = height
        else:
            raise ValueError("Height must be greater than 0!")
    
    @property
    def area(self) -> Union[int, float]:
        """
        Calculate the area of the rectangle.

        Returns:
            Union[int, float]: The area of the rectangle.
        """
        return self.height * self.width
    

if __name__ == "__main__":
    try:
        my_rectangle: Rectangle = Rectangle(5, 10)
        print(f"Szerokość: {my_rectangle.width}")
        print(f"Wysokość: {my_rectangle.height}")
        print(f"Pole prostokąta: {my_rectangle.area}")

        # Próba uzyskania błędu
        print('-'*30)
        print('Sprawdzenie ochrony przed wartościami niedodatnimi:')
        my_rectangle.height = -5
    except ValueError as e:
        print(f"Error: {e}")