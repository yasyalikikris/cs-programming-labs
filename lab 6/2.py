n = int(input())
divisor = 2
while divisor * divisor <= n and n % divisor != 0:
    divisor += 1
if n > 1 and divisor * divisor > n:
    print("Простое")
else:
    print("Не простое")
