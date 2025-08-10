def count_words(text):
    words = text.split()
    word_freq = {}
    for word in words:
        word = word.lower().strip('.,!?')
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def main():
    text = input("Введите текст: ")
    word_counts = count_words(text)
    print("\nЧастота слов:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()