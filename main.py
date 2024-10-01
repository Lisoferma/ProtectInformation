def ceaser_cipher(text, step):
    dictionary = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    max_index = len(dictionary) - 1
    res = []

    for char in text:
        if char == ' ':
            res.append(' ')
            continue

        index_with_step = dictionary.find(char) + step
        new_index = 0

        if index_with_step > max_index:
            new_index = index_with_step - max_index - 1
        elif index_with_step <= max_index:
            new_index = index_with_step

        res.append(dictionary[new_index])

    return ''.join(res)


def ceaser_decipher(text, step):
    dictionary = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    max_index = len(dictionary) - 1
    res = []

    for char in text:
        if char == ' ':
            res.append(' ')
            continue

        index_with_step = dictionary.find(char) - step
        new_index = 0

        if index_with_step < 0:
            new_index = max_index - index_with_step
        elif index_with_step <= max_index:
            new_index = index_with_step

        res.append(dictionary[new_index])

    return ''.join(res)


def ceaser_decipher_bruteforce(text):
    dictionary = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    max_index = len(dictionary) - 1
    res = []

    for step in range(0, max_index):
        for char in text:
            if char == ' ':
                res.append(' ')
                continue

            index_with_step = dictionary.find(char) + step
            new_index = 0

            if index_with_step > max_index:
                new_index = index_with_step - max_index - 1
            elif index_with_step <= max_index:
                new_index = index_with_step

            res.append(dictionary[new_index])

        print(f"{step}: {''.join(res)}")
        res = []


step_input = int(input("Введите сдвиг: "))
text_input = input("Введите текст, который хотите зашифровать: ")

cipher = ceaser_cipher(text_input, step_input)

print("Шифр: " + cipher)
print("Дешифр: " + ceaser_decipher(cipher, step_input))
print("Брутфорс дешифр:")
ceaser_decipher_bruteforce(cipher)
