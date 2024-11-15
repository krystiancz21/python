class MathCalculations:
    """
    A class storing math functions.
    """
    @classmethod
    def natural_num_sum(cls, n: int) -> int:
        """
        Calculates the sum of natural numbers from 1 to n.
        
        Args:
            n (int): The number representing limit of the range.

        Returns:
            int: The sum of natural numbers.
        """
        if n < 0:
            raise ValueError("The number cannot be less than 0!")
        return sum(range(1, n + 1))

    @classmethod
    def calc_factorial(cls, n: int) -> int:
        """
        Calculates the factorial.

        Args:
            n (int): The number to calculate the factorial.
        
        Returns:
            int: The factorial of the number n.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers!")
        if n == 0:
            return 1
        return n * cls.calc_factorial(n - 1)


if __name__ == "__main__":
    n: int = 5
    print(f"Suma liczb naturalnych od 1 do {n}: {MathCalculations.natural_num_sum(n)}")
    print(f"Silnia liczby {n}: {MathCalculations.calc_factorial(n)}")
