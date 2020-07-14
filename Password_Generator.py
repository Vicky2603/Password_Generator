import string
import random

def gen():
    str1 = string.ascii_uppercase  # will display all the uppercase alphabets
    str2 = string.ascii_lowercase # will display all the lowercase alphabets
    str3 = string.digits  # used for digits
    str4 = string.punctuation  # special characters like: {,},(,) and many more
    
    password_length = int(input("Enter the Password Length:\n"))
    s = []
    s.extend(list(str1))
    s.extend(list(str2))
    s.extend(list(str3))
    s.extend(list(str4))

    random.shuffle(s)  # generates randomly of S
    password = ("".join(s[0:password_length]))
    print(password)

print(gen())
