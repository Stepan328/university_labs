def sum_digits(number):
    sum = 0
    modul = abs(number)
    while modul:
        sum += modul % 10
        modul //= 10
    return sum


def average(numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return None


def normalize_text(text):
    text = text.lower().strip()
    while "  " in text:
        text = text.replace("  ", " ")
    return text


def select_numbers(numbers, threshold):
    res = []
    for number in numbers:
        if threshold < abs(number) < threshold * 2:
            res.append(number)
    return res


def is_palindrome(text):
    text = normalize_text(text)
    return text == text[::-1] if text else False
