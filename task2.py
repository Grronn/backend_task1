def stairs(number):
    if(number<1 or number>20):
        print("Введите число от 1 до 20")
    else:
        for i in range (1,number+1):
            quantity_of_whitespace=number-i
            print(' '*quantity_of_whitespace + '#'*i)
print("Введите количество уровней лесенки от 1 до 20")
number = int(input())
stairs(number)