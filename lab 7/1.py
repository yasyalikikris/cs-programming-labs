values = [int(value) for value in input().split()]
corrected = values.copy()
for index in range(len(corrected)):
    if corrected[index] < 0:
        corrected[index] = 0
print(f"Исходные остатки: {values}")
print(f"Исправленные остатки: {corrected}")