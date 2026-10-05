phone = input()
new_phone = (
    phone.replace("+", "")
    .replace(" ", "")
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
)
print(new_phone)