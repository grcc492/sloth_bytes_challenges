def eval_algebra(parts):
    if parts[2] == "x":
        if parts[1] == "+":
            return int(parts[4]) - int(parts[0])
        return int(parts[0]) - int(parts[4])

    if parts[0] == 'x':
        if parts[1] == '+':
            return int(parts[4]) - int(parts[2])
        return int(parts[4]) + int(parts[2])


if __name__ == "__main__":
    equation = input("evalAlgebra: ").strip()
    parts = equation.split()
    if (
        len(parts) != 5
        or parts[3] != "="
        or parts[1] not in ("+", "-")
        or (parts[0] == "x") == (parts[2] == "x")
    ):
        raise ValueError("Equation must be in the form: '<value/x> <+/-> <value/x> = <value>'")

    try:
        int(parts[4])
    except ValueError:
        raise ValueError("result must be an integer")

    try:
        output = eval_algebra(parts)
        print(f"output = {output}")
    except ValueError as e:
        print(f"Error: {e}")
