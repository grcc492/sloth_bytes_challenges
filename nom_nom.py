def nom_nom(arr):
    new_arr = []

    for i, num in enumerate(arr):
        if i > 0:
            if new_arr[-1] > num:
                new_arr[-1] += num

            if new_arr[-1] <= num:
                new_arr.append(num)

        if i == 0:
            new_arr.append(num)

    return new_arr


if __name__ == "__main__":
    arr_list = ([5, 3, 7], [5, 3, 9], [1, 2, 3], [2, 1, 3], [8, 5, 9], [6, 5, 6, 100])

    for arr in arr_list:
        new_arr = nom_nom(arr)
        print(f"output = {new_arr}")
