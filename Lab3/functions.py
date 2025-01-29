# Function to convert grams to ounces
def grams_to_ounces(grams):
    """Converts grams to ounces (1 ounce = 28.3495231 grams)."""
    ounce = 28.3495231 * grams
    print(f"{grams} grams is equal to {ounce:.2f} ounces.")

# Convert 150 grams to ounces
a = 150
grams_to_ounces(a)


# Function to convert Fahrenheit to Celsius
def temp(fahrenheit):
    """Converts Fahrenheit to Celsius using the formula: (F - 32) * 5/9 = C."""
    celsius = (5/9) * (fahrenheit - 32)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")

# Convert 48 Fahrenheit to Celsius
a = 48
temp(a)


# Function to check if a number is prime
def prime(num):
    """Returns True if the number is prime, else False."""
    if num < 2:
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True

# Function to filter prime numbers from a list
def filter_prime(numbers):
    """Filters out prime numbers from a given list of numbers."""
    return [num for num in numbers if prime(num)]

# List of numbers to filter primes from
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = filter_prime(numbers_list)

print("Original list:", numbers_list)
print("Prime numbers:", prime_numbers)


# Function to reverse the words in a sentence
def reverse_words(sentence):
    """Reverses the words in the given sentence."""
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Get user input and reverse the words in the sentence
user_input = input("Enter a sentence: ")
result = reverse_words(user_input)

print("Reversed words in the sentence:", result)
