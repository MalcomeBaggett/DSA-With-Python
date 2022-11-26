# Write a function, anagrams, that takes in two strings as arguments.
# The function should return a boolean indicating whether or not the strings are anagrams.
# Anagrams are strings that contain the same characters, but in any order.


def anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_dict = {}
    s2_dict = {}

    for char in s1:
        if char not in s1_dict:
            s1_dict[char] = 1
        else:
            s1_dict[char] += 1

    for char in s2:
        if char not in s2_dict:
            s2_dict[char] = 1
        else:
            s2_dict[char] += 1

    return s1_dict == s2_dict


def anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False

    s1_dict = {}
    s2_dict = {}

    for char in s1:
        if char not in s1_dict:
            s1_dict[char] = 1
        else:
            s1_dict[char] += 1

    for char in s2:
        if char not in s2_dict:
            s2_dict[char] = 1
        else:
            s2_dict[char] += 1

    for char in s1:
        if s1_dict.get(char) != s2_dict.get(char):
            return False
    return True
