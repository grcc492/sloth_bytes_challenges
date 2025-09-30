import string


def string_to_numbers(cipher):
    cipher_list = [ord(char.lower()) - ord("a") + 1 for char in cipher if char.isalpha()]
    return cipher_list


def keyword_cipher(keyword, cipher):
    alphabet_list = list(string.ascii_lowercase)
    keyword_list = list(keyword.lower())
    cipher_alphabet = keyword_list + [ch for ch in alphabet_list if ch not in keyword_list]
    cipher_list = string_to_numbers(cipher)
    encrypted = [cipher_alphabet[num-1] for num in cipher_list]
    encrypted_message = "".join(encrypted)
    return encrypted_message


if __name__ == "__main__":
    test_list = [
        ("keyword", "abchij"),
        ("purplepineapple", "abc"),
        ("purplepineapple", "abcdefghijklmnop"),
        ("mubashir", "edabit"),
        ("etaoinshrdlucmfwypvbgkjqxz", "abc"),
        ("etaoinshrdlucmfwypvbgkjqxz", "xyz"),
        ("etaoinshrdlucmfwypvbgkjqxz", "aeiou"),
    ]

    for keyword, cipher in test_list:
        output = keyword_cipher(keyword, cipher)
        print(f"output = {output}")
