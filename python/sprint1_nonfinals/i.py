def is_power_of_four(number: int) -> bool:
    power_of_4 = []
    power = 0
    result = 0
    while result < 10000:
        result = 4 ** power
        power_of_4.append(result)
        power += 1
    if number in power_of_4:
        return True
    return False


print(is_power_of_four(int(input())))
