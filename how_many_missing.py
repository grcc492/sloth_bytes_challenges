def how_many_missing(arr):
    arr_len = arr[-1] - arr[0] + 1
    diff = arr_len - len(arr)
    return diff


if __name__ == "__main__":
    arrs = [[1, 2, 3, 8, 9], [1, 3], [7, 10, 11, 12], [1, 3, 5, 7, 9, 11], [5, 6, 7, 8]]

    for arr in arrs:
        missing = how_many_missing(arr)
        print(f"output = {missing}")
