def is_valid_command(command):
    return command in ['0', '1', '2', 'exit']
def can_burn(power, fuel):
    return fuel >= power
def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    fuel -= power
    new_speed = max(0, speed + gravity - thrust_step * power)
    new_height = max(0, height - new_speed)
    return new_height, new_speed, fuel
def get_status(height, speed, safe_speed=2):
    if height > 0:
        return 'В полете'
    return 'Посадка успешна' if speed <= safe_speed else 'Авария'
def format_state(height, speed, fuel):
    return f'Высота: {height} | Скорость: {speed} | Топливо: {fuel}'
def main():
    height, speed, fuel = 28, 4, 10
    gravity, thrust_step = 3, 3
    print(format_state(height, speed, fuel))
    while True:
        command = input().strip()
        if not is_valid_command(command):
            print('Ошибка команды')
            continue
        if command == 'exit':
            print('Полет прерван')
            break
        power = int(command)
        if not can_burn(power, fuel):
            print('Недостаточно топлива')
            continue
        height, speed, fuel = simulate_step(
            height, speed, fuel, power, gravity, thrust_step
        )
        print(format_state(height, speed, fuel))
        status = get_status(height, speed)
        if status != 'В полете':
            print(status)
            break
if __name__ == '__main__':
    main()
