def vigenere(text, key, is_encrypt=True):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
    result = ''

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])
        key_n = alphabet.index(key[i % len(key)])

        if is_encrypt:
            value = (letter_n + key_n) % len(alphabet)
        else:
            value = (letter_n - key_n) % len(alphabet)

        result += alphabet[value]

    return result


text_input = input("Введите текст, который хотите зашифровать: ")
key_input = input("Введите ключ: ")

encrypt = vigenere(text_input, key_input, True)
decrypt = vigenere(encrypt, key_input, False)

print("Шифр: " + encrypt)
print("Дешифр: " + decrypt)
