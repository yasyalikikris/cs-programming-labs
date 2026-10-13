n = int(input())
nize_zero = 0
ravno_zero = 0
vuse_zero = 0
for _ in range(n):
    temp = float(input())
    if temp < 0:
        nize_zero += 1
    elif temp == 0:
        ravno_zero += 1
    else:
        vuse_zero += 1
print(f"Ниже нуля: {nize_zero}")
print(f"Равны нулю: {ravno_zero}")
print(f"Выше нуля: {vuse_zero}")
