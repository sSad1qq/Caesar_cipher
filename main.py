def caesar_cipher(text, shift, direction, language):
    if language == "en":
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif language == "ru":
        alphabet_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        alphabet_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        return "Ле, братишка, ты на каком базаришь дон"



    shift = shift if direction == "шифрование" else -shift

    result = []
    for char in text:
        if char in alphabet_lower:
            new_index = (alphabet_lower.index(char) + shift) % len(alphabet_lower)
            result.append(alphabet_lower[new_index])
        elif char in alphabet_upper:
            new_index = (alphabet_upper.index(char) + shift) % len(alphabet_upper)
            result.append(alphabet_upper[new_index])
        else:
            result.append(char)

    return "".join(result)


print("Шифр Цезаря")
ur_direction = input("Выберите направление (шифрование/дешифрование): ").strip().lower()
ur_language = input("Выберите язык алфавита (ru/en): ").strip().lower()
ur_shift = int(input("Введите шаг сдвига: ").strip())
ur_text = input("Введите текст: ")


result = caesar_cipher(ur_text, ur_shift, ur_direction, ur_language)
print("Результат:", result)