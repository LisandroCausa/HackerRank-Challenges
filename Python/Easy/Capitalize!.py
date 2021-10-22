# https://www.hackerrank.com/challenges/capitalize/problem

# Given a full name, your task is to capitalize the name appropriately.

import math
import os
import random
import re
import sys

def solve(s):
    words = s.split(" ")
    temp_words = []
    for i in words:
        temp_words.append(i.capitalize())

    final_string = ""

    for w in temp_words:
        final_string += w + " "
    
    final_string = final_string.rstrip(final_string[-1])
    return final_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
