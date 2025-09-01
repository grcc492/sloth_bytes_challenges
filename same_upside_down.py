def same_upside_down(num_str: str) -> bool:

    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    for digit in num_str:
        if digit not in mapping:
            return False

    rotated_str = ""
    for digit in reversed(num_str):
        rotated_str += mapping[digit]

    return num_str == rotated_str


if __name__ == '__main__':
    num_str = input("sameUpsidedown: ")
    output = same_upside_down(num_str)
    print(f'output = {output}')
