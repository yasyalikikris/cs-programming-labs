price = float(input())
age = int(input())

if price <= 0 or age < 0 or age > 120:
    print("Ошибка")
elif age <= 5:
    cost = price * 0.0
    print(f"Стоимость: {cost:.2f} руб")
elif age <= 17:
    cost = price * 0.5
    print(f"Стоимость: {cost:.2f} руб")
elif age <= 59:
    cost = price * 1.0
    print(f"Стоимость: {cost:.2f} руб")
else:
    cost = price * 0.7
    print(f"Стоимость: {cost:.2f} руб")
