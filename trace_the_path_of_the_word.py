def get_neighbors(position, target, matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = position
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    neighbors_position = []
    for row_offset, col_offset in directions:
        new_row = row + row_offset
        new_col = col + col_offset
        if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == target:
            neighbors_position.append((new_row, new_col))
    return neighbors_position


def dfs_path_finder(current_position, word, word_index, path_so_far, matrix):
    if word_index == len(word):
        return path_so_far

    next_letter = word[word_index]
    neighbors_position = get_neighbors(current_position, next_letter, matrix)
    for neighbor_position in neighbors_position:
        new_path = path_so_far + [neighbor_position]
        result = dfs_path_finder(neighbor_position, word, word_index + 1, new_path, matrix)
        if result:
            return result

    return None


def trace_the_path_of_the_word(word, matrix):
    starts = []
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            if matrix[row_index][col_index] == word[0]:
                starts.append((row_index, col_index))

    for start in starts:
        path = dfs_path_finder(start, word, 1, [start], matrix)
        if path:
            return path
    return None


if __name__ == "__main__":
    word_matrix_list = [
        ("BISCUIT", [["B", "I", "T", "R"], ["I", "U", "A", "S"], ["S", "C", "V", "W"], ["D", "O", "N", "E"]]),
        ("HELPFUL", [["L", "I", "T", "R"], ["U", "U", "A", "S"], ["L", "U", "P", "O"], ["E", "F", "E", "H"]]),
        ("UKULELE", [["N", "H", "B", "W"], ["E", "X", "A", "D"], ["L", "A", "U", "U"], ["E", "L", "U", "K"]]),
        ("SURVIVAL", [["V", "L", "R", "L"], ["V", "A", "I", "V"], ["I", "O", "S", "C"], ["V", "R", "U", "F"]]),
    ]

    for word, matrix in word_matrix_list:
        path = trace_the_path_of_the_word(word, matrix)
        if path:
            print(f"{word}: {path}")
        else:
            print(f"{word}: Not present")
