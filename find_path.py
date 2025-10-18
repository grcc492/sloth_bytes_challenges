def sort_order(arr):
    arr_sorted = sorted(arr)
    result = [arr_sorted[0][0]]
    used = set()

    while True:
        connected = False
        for flight_from, flight_to in arr_sorted:
            if result[-1] == flight_from and (flight_from, flight_to) not in used:
                result.append(flight_to)
                used.add((flight_from, flight_to))
                connected = True
                break
        if not connected:
            break
    return result


if __name__ == "__main__":
    arrays = [
        [["C", "F"], ["A", "C"], ["I", "Z"], ["F", "I"]],
        [["A", "C"], ["A", "B"], ["C", "B"], ["B", "A"], ["B", "C"]],
        [["Y", "L"], ["D", "A"], ["A", "D"], ["R", "Y"], ["A", "R"]],
    ]
    for arr in arrays:
        result = sort_order(arr)
        print(f"output = {result}")
