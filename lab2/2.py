parts = input().split()

last_name = parts[0].capitalize()
first_initial = parts[1][0].upper()
second_initial = parts[2][0].upper()

print(f"{last_name} {first_initial}. {second_initial}.")