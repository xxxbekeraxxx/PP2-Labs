#Problem 1
from functools import reduce
nums = [2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)


print(" ")
#Problem 2
s = "Hello World"
upper = len([c for c in s if c.isupper()])
lower = len([c for c in s if c.islower()])
print(f"Uppercase: {upper}, Lowercase: {lower}")


print(" ")
#Problem 3
s = "madam"
is_palindrome = s == s[::-1]
print(is_palindrome)


print(" ")
#Problem 4
import math, time
x = 25100
ms = 2123
time.sleep(ms / 1000)
print(f"Square root of {x} after {ms} milliseconds is {math.sqrt(x)}")


print(" ")
#Problem 4
t = (1, 2, 3)
result = all(t)
print(result)
