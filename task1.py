def sum_of_numbers(number):
    odd = 0
    even = 0
    for digit in number:
        int_digit=int(digit)
        if int_digit % 2 == 0:
            even += int_digit
        else:
            odd += int_digit

    return odd, even
number = input()
odd_sum, even_sum = sum_of_numbers(number)
print(odd_sum, even_sum)