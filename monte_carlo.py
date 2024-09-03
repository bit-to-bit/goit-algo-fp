"""Task 7 - Monte Carlo"""
import random
from collections import Counter

NUMBER_OF_IMITATIONS = 10_000_000

random.seed(42)


def roll_dices(number_of_dices):
    result = 0
    for i in range(number_of_dices):
        result += random.randint(1, 6)
    return result


def print_results(imitation_results):
    print(f'{'-'*21}\n|Сума|  Імовіність  |\n{'-'*21}')
    for k, v in sorted(imitation_results.items(), key=None):
        print(f"|{k: >3} | {round(v/NUMBER_OF_IMITATIONS*100,2):10.2f} % |")


if __name__ == "__main__":
    imitation_results = Counter()
    for i in range(0, NUMBER_OF_IMITATIONS):
        imitation_results[roll_dices(2)] += 1
    print_results(imitation_results)
