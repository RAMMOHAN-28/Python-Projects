import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "01234456789"
symbols = "!@#$%^&*7"

all_char = lower + upper + numbers + symbols
length = int(input("Enter a Length:"))

password = ''.join(random.sample(all_char, length))
print("Generated Passowrd:",password)










import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()_+?|<>?/,."

all_char = lower+upper+numbers+symbols 
length = int(input("Enter a length"))

password = ''.join(random.sample(all_char,length))
print("Generated password",password)