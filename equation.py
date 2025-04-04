import math
import sys
import os

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


def get_valid_float(prompt, non_zero=False):
    while True:
        try:
            value = float(input(prompt))
            if non_zero and value == 0:
                raise ValueError
            return value
        except ValueError:
            print("Error. Expected a valid real number.")


def interactive_mode():
    a = get_valid_float("a = ", non_zero=True)
    b = get_valid_float("b = ")
    c = get_valid_float("c = ")
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
    roots = solve_quadratic(a, b, c)
    if len(roots) == 2:
        print(f"There are 2 roots\nx1 = {roots[0]}\nx2 = {roots[1]}")
    elif len(roots) == 1:
        print(f"There are 1 roots\nx1 = {roots[0]}")
    else:
        print("There are 0 roots")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        print("Usage: python equation.py [filename]")
        sys.exit(1)