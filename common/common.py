import random
import string


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return  result_str


def get_random_unique_string(length):
    result_str = ''.join(random.sample(string.ascii_letters, length))
    print("Random unique string of length", length, "is:", result_str)
    return result_str

