from collections import deque


# bfs
def can_exit(matrix, start):
    if matrix[-1][-1] != 0 or matrix[0][0] != 0:
        return False

    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = set()
    neighbors_queue = deque([start])

    while neighbors_queue:
        (row, col) = neighbors_queue.popleft()

        if (row, col) in visited:
            continue
        visited.add((row, col))

        if (row, col) == (rows - 1, cols - 1):
            return True

        for row_offset, col_offset in directions:
            new_row = row + row_offset
            new_col = col + col_offset
            if 0 <= new_row < rows and 0 <= new_col < cols:
                if matrix[new_row][new_col] == 0:
                    neighbors_queue.append((new_row, new_col))

    return False


if __name__ == "__main__":
    matrix_list = [
        ([[0, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 1, 0, 1, 1],
          [1, 0, 0, 0, 0, 1, 1],
          [1, 1, 0, 1, 0, 0, 1],
          [1, 1, 0, 1, 1, 0, 0],]),
        ([[0, 1, 1, 1, 1, 1, 1],
          [0, 0, 1, 0, 0, 1, 1],
          [1, 0, 0, 0, 0, 1, 1],
          [1, 1, 0, 1, 0, 0, 1],
          [1, 1, 0, 0, 1, 1, 1]]),
        ([[0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [1, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 1]]),
        ([[0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [1, 1, 1, 0, 0, 0, 0],
          [1, 0, 0, 0, 1, 1, 0],
          [1, 1, 1, 1, 1, 1, 0]])
    ]

    start = (0, 0)
    for matrix in matrix_list:
        result = can_exit(matrix, start)
        print(f"output = {result}")
