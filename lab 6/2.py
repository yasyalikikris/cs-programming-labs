n = int(input())
chislo = 2
while chislo * chislo <= n and n % chislo != 0:
    chislo += 1
if n > 1 and chislo * chislo > n:
    print("Простое")
else:
    print("Не простое")
