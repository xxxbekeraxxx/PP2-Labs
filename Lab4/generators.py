def generate_squares(N):
    for i in range(N):
        yield i ** 2

N = 10
for square in generate_squares(N):
    print(square)

print("")

def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number n: "))
even_nums = list(even_numbers(n))
print(", ".join(map(str, even_nums)))

print("")

def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input("Enter a number n: "))
for number in divisible_by_3_and_4(n):
    print(number)

print("")

def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2
a = 3
b = 8
for square in squares(a, b):
    print(square)

print("")

def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = 5
for number in countdown(n):
    print(number)




