# Write a function, pair_sum, that takes in a list and a target sum as arguments.
# The function should return a tuple containing a pair of indices whose elements sum to the given target.
# The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair that sums to the target.


def pair_sum(numbers, target_sum):
    dict = {}

    for index in range(0, len(numbers)):
        num = numbers[index]
        target = target_sum - num
        if target in dict:
            return (index, dict[target])
        dict[num] = index


# this solution iterates once and accounts for edge cases when the the two numbers that equal the target sum are the same.
