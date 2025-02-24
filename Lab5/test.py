import re 
pattern = r'[a-z]+(?:_[a-z]+)*'
input_string = input("Input the string: ")
matches = re.findall(pattern, input_string)
for match in matches:
    print(f"Correct answer is or are: '{match}'")