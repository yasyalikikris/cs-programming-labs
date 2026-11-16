R, C = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]
r1, r2, c1, c2 = map(int, input().split())
target = int(input())
res = [(r, c) for r in range(r1, r2 + 1) for c in range(c1, c2 + 1) if table[r][c] == target]
if res:
    for r, c in res:
        print(r, c)
else:
    print("Не найдено")
