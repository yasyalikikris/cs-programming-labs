values = [int(value) for value in input().split()]
squares = [value ** 2 for value in values if value > 0 and value % 2 != 0]
print(f"Квадраты: {squares}")
