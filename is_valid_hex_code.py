def is_valid_hex_code(hex_code: str) -> bool:

    valid_code_set = set("0123456789abcdefABCDEF")

    if len(hex_code) == 7:
        if hex_code.startswith("#"):
            for hex_code_char in hex_code[1:]:
                if hex_code_char in valid_code_set:
                    continue
                return False
            return True
    return False


if __name__ == '__main__':
    num_str = input("is_valid_hex_code: ")
    output = is_valid_hex_code(num_str)
    print(f'output = {output}')
