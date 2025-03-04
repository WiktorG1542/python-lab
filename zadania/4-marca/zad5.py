def transposition_cipher(text: str, key: int):
    if key > len(text):
        return text

    l = []

    for a in range(len(text)):
        new_char = chr(ord(text[a]) + key)
        l.append(new_char)

    return "".join(l)

print(transposition_cipher("hello", 3))
print(transposition_cipher("abc", 2))
print(transposition_cipher("xyz", 1))
print(transposition_cipher("Hello, World!", 5))