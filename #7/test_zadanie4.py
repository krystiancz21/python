from Rectangle import Rectangle
import pytest

def test_init():
    """Test rectangle initialization."""
    rectangle = Rectangle(2, 3)
    assert rectangle.a == 2, "Długość boku a powinna wynosić 2"
    assert rectangle.b == 3, "Długość boku b powinna wynosić 3"

def test_circuit():
    """Test perimeter calculation."""
    rectangle = Rectangle(2, 3)
    assert rectangle.circuit() == 10, "Obwód powinien wynieść 10"

def test_area():
    """Test area calculation."""
    rectangle = Rectangle(2, 3)
    assert rectangle.area() == 6, "Pole powinno wynosić 6"

# Uruchamiamy uzywajac polecenia: pytest test_zadanie4.py / py test_zadanie4.py
if __name__ == "__main__":
    pytest.main(["test_zadanie4.py"])