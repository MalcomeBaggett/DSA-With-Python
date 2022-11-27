# Write a function, most_frequent_char, that takes in a string as an argument.
# The function should return the most frequent character of the string.
# If there are ties, return the character that appears earlier in the string.

# You can assume that the input string is non-empty.


def most_frequent_char(s):
    dict = {}
    max = float("-inf")
    freq_char = ""
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    for val in dict:
        if dict[val] > max:
            max = dict[val]
            freq_char = val
    return freq_char
