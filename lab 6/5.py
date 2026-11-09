n = int(input())
if n < 1 or n > 10:
    print("Ошибка")
else:
    for i in range(n):
        a = []
        for j in range(n):
            if i >= j:
                distance = i - j
            else:
                distance = j - i
            a.append(str(distance))
        print(' '.join(a))