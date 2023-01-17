from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    result = 0
    if (len(temperatures) == 1 or
            (len(temperatures) == 2 and temperatures[0] < temperatures[1])):
        return 1
    if temperatures[-1] > temperatures[-2]:
        result += 1
    if temperatures[0] > temperatures[1]:
        result += 1
    if len(temperatures) == 2 and temperatures[0] == temperatures[1]:
        return 0
    for i in range(1, len(temperatures) - 1):
        if (temperatures[i-1] < temperatures[i] and temperatures[i] >
                temperatures[i+1]):
            result += 1
    return result


# def read_input() -> List[int]:
#     n = int(input())
#     temperatures = list(map(int, input().strip().split()))
#     return temperatures

# temperatures = read_input()
temperatures = [-159, -248, 8, -23, -45, -131, -169, -184, 159, -241]
print(get_weather_randomness(temperatures))


