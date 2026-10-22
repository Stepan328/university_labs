from functions import *

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

assert select_numbers([-5, 0, 2, 5], 2) == []
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3, 4], 2) == [3]
assert select_numbers([-4, -3, -2, -1, 0, 1, 2, 3, 4], 0) == []
original_list = [-5, 0, 2, 5]
copy_list = original_list.copy()
select_numbers(original_list, 2)
assert original_list == copy_list

assert is_palindrome("казак")
assert not(is_palindrome("дуб"))
assert not(is_palindrome(""))
print("Базовые проверки пройдены")
