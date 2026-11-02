n = int(input())
if n < 0:
    print("Ошибка")
else:
    count = 0
    digit_sum = 0
    if n == 0:
        count = 1
    else:
        while n > 0:
            digit = n % 10
            digit_sum += digit
            count += 1
            n //= 10
    print(f"Цифр: {count}")
    print(f"Сумма цифр: {digit_sum}")
