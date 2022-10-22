import string
import random

letters = string.hexdigits
random_letters = random.choice(letters).join(random.choice(letters) for i in range(16))

print(str(random_letters))