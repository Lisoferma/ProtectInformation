def egcd(a, b):
    # Расширенный алгоритм Евклида для нахождения обратного по модулю
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    # Находит обратное к a по модулю m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    else:
        return x % m


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


def affine(text, a, b, is_encrypt=True):
    alphabet = 'аоуынт '
    a_inv = modinv(a, len(alphabet))
    result = ''

    for i in range(len(text)):
        letter_n = alphabet.index(text[i])

        if is_encrypt:
            value = (a * letter_n + b) % len(alphabet)
        else:
            value = ((letter_n - b) * a_inv) % len(alphabet)

        result += alphabet[value]

    return result


print("Алфавит: аоуынт_")

text_input = input("Введите текст, который хотите зашифровать: ")
a_input = int(input("Введите a: "))
b_input = int(input("Введите b: "))

encrypt = affine(text_input, a_input, b_input, True)
decrypt = affine(encrypt, a_input, b_input, False)

print("Шифр: " + encrypt)
print("Дешифр: " + decrypt)

# a = 5
# N = 34
