def convert_to_title(num):
    result = []
    while num > 0:
        num, remainder = divmod(num - 1, 26)
        result.append(chr(remainder + ord("A")))
    return "".join(reversed(result))


if __name__ == "__main__":
    try:
        num = int(input("Enter a positive whole number: "))
        if num < 1:
            raise ValueError("must be greater than 0")
        output = convert_to_title(num)
        print(f'output = "{output}"')
    except ValueError as e:
        print(f"Invalid input: must be a positive whole number ({e})")
