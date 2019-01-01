# https://projecteuler.net/problem=1
# Multiples of 3 and 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def check_multiply_three(number):
    if number % 3 == 0:
        return True
    else:
        return False


def check_multiply_five(number):
    if number % 5 == 0:
        return True
    else:
        return False


def multiply_below_thousand():
    sum_below_1000 = 0
    for i in range(1000):
        if check_multiply_three(i) or check_multiply_five(i):
            sum_below_1000 += i
    return sum_below_1000


print(multiply_below_thousand())
