import ast


def maximum_seating(seating_chart: list) -> int:
    n = len(seating_chart)
    seated_count = 0

    for i in range(n):
        # Skip if seat is already occupied
        if seating_chart[i] != 0:
            continue

        # Check if all seats within 2 positions are empty
        can_seat = True
        for j in range(max(0, i-2), min(n, i+3)):
            if j != i and seating_chart[j] == 1:
                can_seat = False
                break

        if can_seat:
            seating_chart[i] = 1
            seated_count += 1

    return seated_count


if __name__ == "__main__":
    raw_input_str = input("maximum_seating: ")
    try:
        seating_chart = ast.literal_eval(raw_input_str)
    except (SyntaxError, ValueError):
        raise ValueError("Invalid format! Please enter something like: [0,0,0,1,0,0,1,0,0,0]")

    if not isinstance(seating_chart, list):
        raise TypeError("Input must be a list, e.g., [0,0,0,1,0,0,1]")

    if not all(i in (0, 1) for i in seating_chart):
        raise ValueError("List must contain only 0 or 1")

    output = maximum_seating(seating_chart)
    print(f"output = {output}")
