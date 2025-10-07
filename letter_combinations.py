import itertools


def letterCombinations(nums, keypad):
    if not nums:
        return []

    invalid_keys = [num for num in nums if num not in keypad]
    if invalid_keys:
        raise ValueError(f"Invalid keypad digits: {invalid_keys}")

    letters_list = [list(keypad[num]) for num in nums]

    result = ["".join(p) for p in itertools.product(*letters_list)]

    return result


if __name__ == "__main__":
    keypad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    nums_list = ["23", "", "2", "27", "234", "79", "109"]
    for nums in nums_list:
        try:
            result = letterCombinations(nums, keypad)
            print(f"output = {result}")
        except ValueError as e:
            print(f"{nums}: Error - {e}")
