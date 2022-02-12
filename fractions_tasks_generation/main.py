from math import ceil, floor, log10
from random import randint

from representable_fraction import RepresentableFraction as RFraction


def fairly_random_value():
    """
    Helps to create more fair fractions.

    If I random a denominator between 1 and 10**3, there will
    only be 0.099 chance of a sample below 100 and that's
    unfair for that, who will have to decompose to primes.
    """
    max_degree = randint(0, 1)
    return randint(10**max_degree, 10**(max_degree + 1))


def randomize_bool():
    return bool(randint(0, 1))


###########################
## CONFIGURATION SECTION ##
###########################
actions = {
    '+': {
        'amount': 5
    },
    '-': {
        'amount': 5
    },
    'cdot': {
        'amount': 5
    },
    ':': {
        'amount': 5
    },
}

USE_NEGATIVES = False

########################
## GENERATION SECTION ##
########################
tasks = []
answers = []

for action in actions:
    for task_num in range(actions[action]['amount']):
        numerator1 = fairly_random_value()
        denominator1 = fairly_random_value()
        fraction1 = RFraction(numerator1, denominator1)

        numerator2 = fairly_random_value()
        denominator2 = fairly_random_value()
        fraction2 = RFraction(numerator2, denominator2)

        if action == '-' and fraction1 < fraction2:
            fraction1, fraction2 = fraction2, fraction1
        task = f'{fraction1.to_LO_format(randomize_bool())} {action} {fraction2.to_LO_format(randomize_bool())}'

        if action == '+':
            result = fraction1 + fraction2
        elif action == '-':
            result = fraction1 - fraction2
        elif action == 'cdot':
            result = fraction1 * fraction2
        elif action == ':':
            result = fraction1 / fraction2

        answer = f'{task} = {result.to_LO_format(True, True)}'

        tasks.append(task)
        answers.append(answer)

print('\n'.join(tasks))
print('\n============\n')
print('\n'.join(answers))
