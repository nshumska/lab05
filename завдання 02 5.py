def count_word_occurrences(input_text):
    word_count = {}
    words = input_text.split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
        print(word_count[word] - 1, end=' ')

if __name__ == "__main__":
    # Зчитуємо вміст файлу
    with open("input.txt", "r", encoding="utf-8") as file:
        input_text = file.read()

    # Викликаємо функцію для підрахунку входжень слів
    count_word_occurrences(input_text)
