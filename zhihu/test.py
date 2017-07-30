# encoding: utf-8

import random

luck_numbers = []

users = map(str, range(33))
moneys = [8, 8, 2, 1, 2, 1, 8, 8, 1, 8, 2, 1, 4, 2, 2,
          2, 2, 2, 8, 1, 2, 2, 2, 1, 2, 2, 1, 2, 1, 2,
          2, 1, 2]

data = dict(zip(users, moneys))
for user, amount in data.items():
    luck_numbers.extend([user] * amount)

random.shuffle(luck_numbers)
print(luck_numbers)
print(random.choice(luck_numbers))
