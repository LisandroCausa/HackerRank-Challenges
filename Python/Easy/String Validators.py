# https://www.hackerrank.com/challenges/string-validators/problem

# In the first line, print True if STRING has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if STRING has any alphabetical characters. Otherwise, print False.
# In the third line, print True if STRING has any digits. Otherwise, print False.
# In the fourth line, print True if STRING has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if STRING has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    alphanumeric = False
    alphabetical = False
    digits = False
    lowercase = False
    uppercase = False
    s = input()

    for c in s:
        if c.isalnum():
            alphanumeric = True
        if c.isalpha():
            alphabetical = True
        
        if c.isdigit():
            digits = True
        elif c.islower():
            lowercase = True
        elif c.isupper():
            uppercase = True

    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)