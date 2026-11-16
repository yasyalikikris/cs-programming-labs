values = [int(value) for value in input().split()]
target = int(input())
indexes = []
for index,value in enumerate(values):
    if value == target:
        indexes.append(index)
print(f"Индексы: {indexes}")