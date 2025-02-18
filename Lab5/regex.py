#Problem 1
import re
test_str = ["a", "ab", "abb", "abbbbb", "b", "ba", "acd"]
pattern = r"ab*"

for string in test_str:
    if re.match(pattern, string):
        print(f"'{string}' соответствует шаблону")
    else:
        print(f"'{string}' не соответствует шаблону")

print()  
#Problem 2
import re
test_str = ["a", "ab", "abb", "abbb", "abbbbb", "cd", "ac", "as"]
pattern = r"ab{2,3}$"

for string in test_str:
    if re.match(pattern, string):
        print(f"'{string}', соответствует шаблону")
    else:
        print(f"'{string}', не соответствует шаблону")

