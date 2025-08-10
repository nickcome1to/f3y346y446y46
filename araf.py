def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


def main():
    print("Проверка, является ли строка палиндромом")
    text = input("Введите строку: ")
    if is_palindrome(text):
        print(f"'{text}' - это палиндром!")
    else:
        print(f"'{text}' - это не палиндром!")


if __name__ == "__main__":
    main()