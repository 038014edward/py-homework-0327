import random


def generate_random_number():
    numbers = []
    # random_number = 0
    for i in range(8):
        random_number = random.randint(1, 15)
        while random_number in numbers:
            random_number = random.randint(1, 15)
        numbers.append(random_number)
    return numbers


print(generate_random_number())
