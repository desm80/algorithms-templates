from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter = ''.join(sorted(shorter))
    longer = ''.join((sorted(longer)))
    for i in range(len(shorter)):
        if shorter[i] != longer[i]:
            return longer[i]
    return longer[-1]


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

# shorter, longer = read_input()
# print(get_excessive_letter(shorter, longer))
print(get_excessive_letter('go', 'ogg'))
