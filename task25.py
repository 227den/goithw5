import re

def generator_numbers(text: str):
    pattern = r'\b\d+(?:\.\d+)?\b'
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: callable):
    total_profit = sum(func(text))
    return total_profit