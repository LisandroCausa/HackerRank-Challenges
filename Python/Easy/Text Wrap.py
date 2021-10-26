# https://www.hackerrank.com/challenges/text-wrap/problem

# You are given a string S and width W.
# Your task is to wrap the string into a paragraph of width W.

import textwrap

def wrap(string, max_width):
    new_string = ""
    iterator = 0
    for c in string:
        new_string += c
        iterator += 1
        if iterator >= max_width:
            new_string += "\n"
            iterator = 0

    return new_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)