from collections import deque


def can_reach_exit(grid):
    start = end = None
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@":
                start = (r, c)
            if grid[r][c] == "E":
                end = (r, c)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = set()
    neighbors_queue = deque([start])

    while neighbors_queue:
        (row, col) = neighbors_queue.popleft()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for row_offset, col_offset in directions:
            new_row = row + row_offset
            new_col = col + col_offset

            if (new_row, new_col) == end:
                return True

            if 0 <= new_row < rows and 0 <= new_col < cols:
                if grid[new_row][new_col] == ".":
                    neighbors_queue.append((new_row, new_col))

    return False


if __name__ == "__main__":
    grids = [
        ["@..", ".#E", "..."],
        ["@#E"],
        ["@.#.", "..#E", "####"],
        ["@...", ".###", "...E"]
    ]

    for grid in grids:
        result = can_reach_exit(grid)
        print(f"output = {result}")
