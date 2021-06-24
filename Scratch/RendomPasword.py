import string
from random import *

characters = string.ascii_letters + string.punctuation + string.digits
passw = string.ascii_letters + string.punctuation + string.digits
n = int(input("How long do you want your password:"))

password = "".join(choice(passw) for x in range(randint(8, n + 1)))
print(password)