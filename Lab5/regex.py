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


print()  
#Problem 3
import re
s = "this_is_a_test example_not_match"
print(re.findall(r'[a-z]+(?:_[a-z]+)+', s))


print()  
#Problem 4
import re
s = "Hello World"
print(re.findall(r'[A-Z][a-z]+', s))


print()  
#Problem 5
import re
s = "a_example_b"
print(re.match(r'a.*b$', s))

print()  
#Problem 6
import re
s = "Hello, world. This is a test."
print(re.sub(r'[ ,.]', ':', s))


print()  
#Problem 7
import re
s = "snake_case_example"
print(re.sub(r'_(.)', lambda x: x.group(1).upper(), s))



print()  
#Problem 8
import re
s = "HelloWorld"
print(re.findall(r'[A-Z][^A-Z]*', s))


print()  
#Problem 9
import re
s = "HelloWorld"
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', s))


print()  
#Problem 10
import re
s = "camelCaseExample"
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower())

