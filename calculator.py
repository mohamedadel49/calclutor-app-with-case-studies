def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def sub(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def mul(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def div(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ValueError on zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main() -> None:
    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
    }

    print("Simple Calculator (+, -, *, /)")
    op = input("Choose operation (+, -, *, /): ").strip()
    if op not in operations:
        print("Invalid operation.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = operations[op](num1, num2)
        print(f"Result: {result}")
    except ValueError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
