import random

class RandomChooser:
    def choose_a(self, *vals_list):
        random_index = random.randint(0, len(vals_list) - 1)
        return vals_list[random_index]