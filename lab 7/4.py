rows, columns = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(rows)]
row_sums = [sum(row) for row in table]
column_sums = [sum(col) for col in zip(*table)]
print(f"Суммы строк: {row_sums}")
print(f"Суммы столбцов: {column_sums}")
