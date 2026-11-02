n = int(input())
odd_count = 0
for r in range(n):
    val = 1
    for k in range(r + 1):
        print(val, end=" ")
        if val%2!=0:
            odd_count += 1
        val = val * (r - k) // (k + 1)
    print()
print(f"Нечетных элементов: {odd_count}")
