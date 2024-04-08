# coding=windows-1251
def guess_number(min,max):
    while True:
        guess = (min + max) // 2
        print(f"Это число {guess}?")
        answer = input("больше, меньше или верно: ")
        if answer == "верно":
            print("Число угадано")
            break
        elif answer == "больше":
            min = guess + 1
        elif answer == "меньше":
            max = guess - 1
        else:
            print("Введите больше, меньше или верно")
print("Загадайте число от 1 до 100")
guess_number(1,100)