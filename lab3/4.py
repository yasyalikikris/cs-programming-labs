train, gorod1, gorod2, time, price = input().split(";")

formatted_price = f"{float(price):.2f}"

print(f"Поезд: {train}")
print(f"Маршрут: {gorod1} - {gorod2}")
print(f"Отправление: {time}")
print(f"Цена: {formatted_price} руб")