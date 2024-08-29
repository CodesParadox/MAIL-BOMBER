import random
import string

emailfirst = "tmhrust"
emaillast = "@gmail.com"

def genuser():
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    return random_string

def getmail():
    random_int = random.randint(10000000, 99999999)
    email = f"{emailfirst}+{random_int}{emaillast}"
    return email