import random


def guess_number():
    secret = random.randint(1, 100)
    attempts = 0
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        try:
            guess = int(input("Введи число: "))
            attempts += 1
            if guess < secret:
                print("Слишком мало!")
            elif guess > secret:
                print("Слишком много!")
            else:
                print(f"Поздравляю! Ты угадал число {secret} за {attempts} попыток!")
                break
        except ValueError:
            print("Введи целое число!")


guess_number()