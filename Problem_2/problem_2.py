# https://projecteuler.net/problem=2
# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated
# by adding the previous two terms. By starting with 1
# and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million, find the
# sum of the even-valued terms.


def check_number_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def fibonacci(n):
    prev_number = 0
    next_number = 1
    sum_of_even_numbers_below_4millions = 0
    while next_number < n:
        number = prev_number + next_number
        prev_number = next_number
        next_number = number
        if check_number_even(number):
            sum_of_even_numbers_below_4millions += number
    return sum_of_even_numbers_below_4millions


print(fibonacci(4000000))
