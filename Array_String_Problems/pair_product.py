# Write a function, pair_product, that takes in a list and a target product as arguments.
# The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

# Be sure to return the indices, not the elements themselves.

# There is guaranteed to be one such pair whose product is the target.


def pair_product(numbers, target_product):
    dict = {}

    for index in range(0, len(numbers)):
        num = numbers[index]
        target = target_product / num
        if target in dict:
            return (index, dict[target])
        dict[num] = index
