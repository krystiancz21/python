class Rectangle:
    def __init__(self, a: float, b: float):
        """Create rectangle with sides a and b."""
        self.a = a
        self.b = b
    
    def circuit(self) -> float:
        """Calculate rectangle's perimeter."""
        return 2 * (self.a + self.b)
    
    def area(self) -> float:
        """Calculate rectangle's area."""
        return self.a * self.b
