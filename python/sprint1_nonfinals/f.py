import re

def is_palindrome(line: str) -> bool:
    new_line = re.sub(r'[^\w\s]', '', line).lower().replace(' ', '')
    if new_line == new_line[::-1]:
        return True
    else:
        return False

print(is_palindrome(input().strip()))

