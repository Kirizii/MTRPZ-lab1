import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Error. a cannot be 0")

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)
    elif discriminant == 0:
        x1 = -b / (2 * a)
        return (x1,)
    else:
        return ()