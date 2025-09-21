import numpy as np


def main():
    # Алфавит и строка-оригинал
    alphabet = ['А', 'О', 'У', 'Ы', 'Н', 'Т', '_']
    text = "У_НАТЫ_ТОННЫ"

    # Параметры шифра
    N = len(alphabet)  # Длина алфавита = 7
    m = 3  # Размер блока

    # Ключевая матрица A (3x3)
    A = np.array([[1, 5, 3],
                  [1, 6, 2],
                  [0, 1, 0]])

    # Вектор сдвига H
    H = np.array([1, 2, 3])

    print("Алфавит:", alphabet)
    print("Длина алфавита N =", N)
    print("Исходный текст:", text)
    print("Ключевая матрица A:\n", A)
    print("Вектор сдвига H:", H)

    # Шифрование
    encrypted = hill_encrypt(text, alphabet, A, H, m)
    print("Зашифрованный текст:", encrypted)

    # Дешифрование
    decrypted = hill_decrypt(encrypted, alphabet, A, H, m)
    print("Расшифрованный текст:", decrypted)


def text_to_numbers(text, alphabet):
    """Преобразование текста в числовой формат"""
    return [alphabet.index(char) for char in text]


def numbers_to_text(numbers, alphabet):
    """Преобразование чисел обратно в текст"""
    return ''.join([alphabet[num] for num in numbers])


def pad_text(text, block_size, alphabet):
    """Добавление padding'а для выравнивания длины текста"""
    padded_text = text
    while len(padded_text) % block_size != 0:
        padded_text += '_'  # Добавляем '_' для padding'а
    return padded_text


def mod_inverse(a, m):
    """Вычисление модульного обратного"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def get_inverse_matrix(matrix, mod):
    """Получение обратной матрицы по модулю"""
    det = int(np.round(np.linalg.det(matrix)))
    det_mod = det % mod

    # Проверяем, что определитель обратим по модулю
    if gcd(det_mod, mod) != 1:
        raise ValueError("Определитель матрицы не обратим по модулю")

    # Вычисляем обратную матрицу
    inv_det = mod_inverse(det_mod, mod)
    adjugate = np.round(np.linalg.det(matrix) * np.linalg.inv(matrix)).astype(int) % mod
    inv_matrix = (inv_det * adjugate) % mod

    return inv_matrix


def gcd(a, b):
    """Наибольший общий делитель"""
    while b:
        a, b = b, a % b
    return a


def hill_encrypt(plaintext, alphabet, A, H, block_size):
    """Шифрование текста методом Хилла"""
    N = len(alphabet)

    # Подготовка текста
    prepared_text = pad_text(plaintext, block_size, alphabet)
    numbers = text_to_numbers(prepared_text, alphabet)

    cipher_numbers = []

    # Шифрование по блокам
    for i in range(0, len(numbers), block_size):
        block = np.array(numbers[i:i + block_size])

        # Y = (X * A + H) mod N
        encrypted_block = (np.dot(block, A) + H) % N
        cipher_numbers.extend(encrypted_block)

    return numbers_to_text(cipher_numbers, alphabet)


def hill_decrypt(ciphertext, alphabet, A, H, block_size):
    """Дешифрование текста методом Хилла"""
    N = len(alphabet)

    # Получаем обратную матрицу
    A_inv = get_inverse_matrix(A, N)

    numbers = text_to_numbers(ciphertext, alphabet)
    plain_numbers = []

    # Дешифрование по блокам
    for i in range(0, len(numbers), block_size):
        block = np.array(numbers[i:i + block_size])

        # X = ((Y - H) * A^{-1}) mod N
        decrypted_block = (np.dot(block - H, A_inv)) % N
        plain_numbers.extend(decrypted_block)

    return numbers_to_text(plain_numbers, alphabet)


if __name__ == "__main__":
    main()