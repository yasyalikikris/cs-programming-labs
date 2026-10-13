n = int(input())
odd_count = 0
for r in range(n):
    val = 1
    for k in range(r + 1):
        if val%2!=0:
            odd_count += 1
        if k == r:
            print(val)
        else:
            print(val, end=" ")
        val = val * (r - k) // (k + 1)
print(f"Нечетных элементов: {odd_count}")
