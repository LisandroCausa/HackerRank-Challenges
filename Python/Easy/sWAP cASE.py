# https://www.hackerrank.com/challenges/swap-case/problem

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    new_string = ""
    for char in s:
        if char.islower():
            new_string = new_string + char.upper()
        else:
            new_string = new_string + char.lower()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)