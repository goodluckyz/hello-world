import random
import string

# Generate 100 random characters
random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
print(random_string)