import random


class Roll:
    roll = []

    def __init__(self, num):
        for n in range(num):
            self.roll.append(random.randint(1, 6))

    def get_roll(self):
        return self.roll
